import numpy as np
import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense, Dropout, Concatenate
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


class LSTMDirectionClassifier:
    """
    LSTM-based direction classifier for multi-horizon prediction.
    Predicts BULLISH/NOT BULLISH for multiple time horizons simultaneously.
    Optimized for identifying long entry points.
    Uses market regime clustering as additional context.
    """
    
    def __init__(self,
                 lookback_window=60,
                 prediction_horizons=[1, 3, 5, 10],
                 lstm_units=64,
                 num_layers=2,
                 dropout=0.3,
                 epochs=50,
                 batch_size=32,
                 learning_rate=0.001,
                 n_clusters=5,
                 verbose=1):
        """
        Parameters:
        -----------
        lookback_window : int
            Number of previous candles to use as input (default: 60)
        prediction_horizons : list
            List of horizons to predict [1, 3, 5, 10] days
        lstm_units : int
            Number of LSTM units per layer
        num_layers : int
            Number of LSTM layers to stack
        dropout : float
            Dropout rate for regularization
        epochs : int
            Maximum training epochs
        batch_size : int
            Training batch size
        learning_rate : float
            Learning rate for Adam optimizer
        n_clusters : int
            Number of market regime clusters (default: 5)
        verbose : int
            Verbosity level (0, 1, 2)
        """
        self.lookback_window = lookback_window
        self.prediction_horizons = prediction_horizons
        self.lstm_units = lstm_units
        self.num_layers = num_layers
        self.dropout = dropout
        self.epochs = epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.n_clusters = n_clusters
        self.verbose = verbose
        
        # Class definitions - BINARY CLASSIFICATION
        self.classes = ['NOT BULLISH', 'BULLISH']
        self.n_classes = 2
        
        # Thresholds for BULLISH classification (need to exceed this to be bullish)
        self.thresholds = {
            1: 0.005,   # >0.5% gain for 1-day
            3: 0.010,   # >1.0% gain for 3-day
            5: 0.015,   # >1.5% gain for 5-day
            10: 0.020,  # >2.0% gain for 10-day
        }
        
        self.model = None
        self.scaler = StandardScaler()
        self.cluster_model = None
        self.cluster_scaler = StandardScaler()
        self.is_fitted = False
        self.training_history = None
        
    def _calculate_rsi(self, data, period=14):
        """Calculate RSI indicator"""
        close_delta = data['Close'].diff()
        
        gain = close_delta.where(close_delta > 0, 0)
        loss = -close_delta.where(close_delta < 0, 0)
        
        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()
        
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi.fillna(50)  # Fill NaN with neutral value
    
    def _calculate_features(self, data):
        """
        Calculate features including OHLCV returns and RSI.
        
        Parameters:
        -----------
        data : pd.DataFrame
            OHLCV data
            
        Returns:
        --------
        features : pd.DataFrame
            Feature dataframe with returns and RSI
        """
        features = pd.DataFrame(index=data.index)
        
        # OHLCV percentage returns
        for col in ['Open', 'High', 'Low', 'Close', 'Volume']:
            features[f'{col}_return'] = data[col].pct_change().fillna(0)
        
        # RSI indicator
        features['RSI_14'] = self._calculate_rsi(data) / 100.0  # Normalize to 0-1
        
        # Keep original close for labeling
        features['Close'] = data['Close']
        
        return features
    
    def _fit_clustering(self, data):
        """
        Fit K-Means clustering on market regimes.
        Clusters based on RSI, volatility (ATR-like), and trend.
        
        Parameters:
        -----------
        data : pd.DataFrame
            Feature data
        """
        if self.verbose:
            print(f"\nFitting {self.n_clusters} market regime clusters...")
        
        # Calculate clustering features for each lookback window
        cluster_features_list = []
        
        for i in range(self.lookback_window, len(data)):
            window = data.iloc[i-self.lookback_window:i]
            
            # Features for clustering
            avg_rsi = window['RSI_14'].mean()
            volatility = window['Close_return'].std()
            trend = (window['Close'].iloc[-1] / window['Close'].iloc[0] - 1)  # Overall return
            
            cluster_features_list.append([avg_rsi, volatility, trend])
        
        cluster_features = np.array(cluster_features_list)
        
        # Fit scaler and cluster model
        cluster_features_scaled = self.cluster_scaler.fit_transform(cluster_features)
        self.cluster_model = KMeans(n_clusters=self.n_clusters, random_state=42, n_init=10)
        self.cluster_model.fit(cluster_features_scaled)
        
        if self.verbose:
            print(f"✓ Clustering complete")
            print(f"  Cluster centers:\n{self.cluster_model.cluster_centers_}")
    
    def _get_cluster_id(self, window):
        """
        Get cluster ID for a single lookback window.
        
        Parameters:
        -----------
        window : pd.DataFrame
            Lookback window of features
            
        Returns:
        --------
        cluster_id : int
            Cluster assignment (0 to n_clusters-1)
        """
        avg_rsi = window['RSI_14'].mean()
        volatility = window['Close_return'].std()
        trend = (window['Close'].iloc[-1] / window['Close'].iloc[0] - 1)
        
        features = np.array([[avg_rsi, volatility, trend]])
        features_scaled = self.cluster_scaler.transform(features)
        cluster_id = self.cluster_model.predict(features_scaled)[0]
        
        return cluster_id
    
    def _create_labels(self, data, horizon):
        """
        Create classification labels (BULLISH/NOT BULLISH) for a specific horizon.
        Labels are ABSOLUTE - all based on current day (day 0).
        
        Parameters:
        -----------
        data : pd.DataFrame
            Feature data with 'Close' column
        horizon : int
            Prediction horizon in days
            
        Returns:
        --------
        labels : np.ndarray
            Integer labels: 0=NOT BULLISH, 1=BULLISH
        """
        # Calculate future return (absolute from current day)
        future_returns = data['Close'].pct_change(horizon).shift(-horizon)
        
        threshold = self.thresholds.get(horizon, 0.01)
        
        # Create binary labels: BULLISH if future return exceeds threshold
        labels = np.where(future_returns > threshold, 1, 0)  # 1=BULLISH, 0=NOT BULLISH
        
        return labels
    
    def _create_sequences(self, features, include_cluster=True):
        """
        Create input sequences with cluster IDs and labels for all horizons.
        
        Parameters:
        -----------
        features : pd.DataFrame
            Feature dataframe
        include_cluster : bool
            Whether to include cluster ID as feature
            
        Returns:
        --------
        X : np.ndarray
            Input sequences (n_sequences, lookback_window, n_features)
        y_dict : dict
            Labels for each horizon {1: labels_1day, 3: labels_3day, ...}
        cluster_ids : np.ndarray
            Cluster IDs for each sequence
        """
        # Extract feature columns (exclude Close which is only for labeling)
        feature_cols = [col for col in features.columns if col != 'Close']
        feature_data = features[feature_cols].values
        
        n_samples = len(features)
        max_horizon = max(self.prediction_horizons)
        
        # Calculate valid sequences
        n_sequences = n_samples - self.lookback_window - max_horizon + 1
        
        if n_sequences <= 0:
            raise ValueError(f"Not enough data. Need at least {self.lookback_window + max_horizon} samples.")
        
        # Calculate number of features (6 OHLCV returns + RSI + optionally cluster)
        n_features = len(feature_cols)
        if include_cluster:
            n_features += 1
        
        # Pre-allocate arrays
        X = np.zeros((n_sequences, self.lookback_window, n_features), dtype=np.float32)
        cluster_ids = np.zeros(n_sequences, dtype=np.int32)
        y_dict = {h: np.zeros(n_sequences, dtype=np.int32) for h in self.prediction_horizons}
        
        # Create sequences
        for i in range(n_sequences):
            start_idx = i
            end_idx = i + self.lookback_window
            
            # Get window
            window_features = feature_data[start_idx:end_idx]
            window_df = features.iloc[start_idx:end_idx]
            
            # Get cluster ID
            if include_cluster:
                cluster_id = self._get_cluster_id(window_df)
                cluster_ids[i] = cluster_id
                
                # Add cluster as one-hot encoded feature across all timesteps
                cluster_one_hot = np.zeros((self.lookback_window, 1))
                cluster_one_hot[:, 0] = cluster_id / self.n_clusters  # Normalize
                
                X[i] = np.concatenate([window_features, cluster_one_hot], axis=1)
            else:
                X[i] = window_features
            
            # Create labels for each horizon
            for horizon in self.prediction_horizons:
                labels = self._create_labels(features, horizon)
                y_dict[horizon][i] = labels[end_idx - 1]
        
        return X, y_dict, cluster_ids
    
    def _build_model(self, input_shape):
        """
        Build multi-task LSTM model with separate output heads for each horizon.
        
        Parameters:
        -----------
        input_shape : tuple
            (lookback_window, n_features)
        """
        # Input layer
        inputs = Input(shape=input_shape, name='input')
        
        # LSTM layers
        x = inputs
        for i in range(self.num_layers):
            return_sequences = (i < self.num_layers - 1)
            x = LSTM(
                self.lstm_units,
                return_sequences=return_sequences,
                name=f'lstm_{i+1}'
            )(x)
            x = Dropout(self.dropout, name=f'dropout_{i+1}')(x)
        
        # Shared dense layer
        shared = Dense(32, activation='relu', name='shared_dense')(x)
        
        # Separate output heads for each horizon
        outputs = []
        output_names = []
        
        for horizon in self.prediction_horizons:
            output = Dense(
                self.n_classes,
                activation='softmax',
                name=f'output_{horizon}day'
            )(shared)
            outputs.append(output)
            output_names.append(f'output_{horizon}day')
        
        # Create model
        model = Model(inputs=inputs, outputs=outputs, name='LSTM_Direction_Classifier')
        
        # Calculate class weights (assume some imbalance towards UP in stock market)
        # This will be refined during training based on actual data
        class_weight = {0: 1.2, 1: 1.0, 2: 1.0}  # Slightly boost DOWN class
        
        # Compile with separate losses for each output
        losses = {name: 'sparse_categorical_crossentropy' for name in output_names}
        metrics = {name: 'accuracy' for name in output_names}
        
        model.compile(
            optimizer=Adam(learning_rate=self.learning_rate),
            loss=losses,
            metrics=metrics
        )
        
        return model
    
    def fit(self, data, validation_split=0.2, early_stopping_patience=10):
        """
        Train the LSTM direction classifier.
        
        Parameters:
        -----------
        data : pd.DataFrame
            OHLCV DataFrame with columns: Open, High, Low, Close, Volume
        validation_split : float
            Fraction of data to use for validation
        early_stopping_patience : int
            Patience for early stopping
            
        Returns:
        --------
        history : keras History object
            Training history
        """
        if self.verbose:
            print("="*80)
            print("TRAINING LSTM DIRECTION CLASSIFIER")
            print("="*80)
            print(f"\n📊 Data: {len(data)} samples")
            print(f"🎯 Prediction horizons: {self.prediction_horizons} days")
            print(f"🏗️  Lookback window: {self.lookback_window} days")
            print(f"🔧 Architecture: {self.num_layers} LSTM layers × {self.lstm_units} units")
            print(f"📈 Classes: {self.classes}")
            print(f"🎲 Market regimes: {self.n_clusters} clusters\n")
        
        # Calculate features
        features = self._calculate_features(data)
        
        # Fit clustering model
        self._fit_clustering(features)
        
        # Create sequences with cluster IDs
        X, y_dict, cluster_ids = self._create_sequences(features, include_cluster=True)
        
        # Scale features
        n_sequences, lookback, n_features = X.shape
        X_reshaped = X.reshape(-1, n_features)
        X_scaled = self.scaler.fit_transform(X_reshaped)
        X = X_scaled.reshape(n_sequences, lookback, n_features)
        
        if self.verbose:
            print(f"\n📦 Training data shape:")
            print(f"   X: {X.shape}")
            for horizon in self.prediction_horizons:
                print(f"   y_{horizon}day: {y_dict[horizon].shape}")
            
            # Print class distribution
            print(f"\n📊 Class distributions:")
            for horizon in self.prediction_horizons:
                unique, counts = np.unique(y_dict[horizon], return_counts=True)
                dist = dict(zip([self.classes[i] for i in unique], counts))
                print(f"   {horizon}-day: {dist}")
        
        # Build model
        self.model = self._build_model(input_shape=(self.lookback_window, n_features))
        
        if self.verbose:
            print(f"\n🏗️  Model architecture:")
            self.model.summary()
        
        # Prepare training data
        y_train = {f'output_{h}day': y_dict[h] for h in self.prediction_horizons}
        
        # Callbacks
        callbacks = [
            EarlyStopping(
                monitor='val_loss',
                patience=early_stopping_patience,
                restore_best_weights=True,
                verbose=self.verbose
            )
        ]
        
        # Train
        if self.verbose:
            print(f"\n🚀 Starting training...")
        
        history = self.model.fit(
            X, y_train,
            epochs=self.epochs,
            batch_size=self.batch_size,
            validation_split=validation_split,
            callbacks=callbacks,
            verbose=self.verbose
        )
        
        self.is_fitted = True
        self.training_history = history
        
        if self.verbose:
            print(f"\n✓ Training complete!")
            print(f"  Epochs trained: {len(history.history['loss'])}")
        
        return history
    
    def predict(self, data, return_probabilities=False):
        """
        Predict direction for all horizons.
        
        Parameters:
        -----------
        data : pd.DataFrame
            OHLCV data to predict on
        return_probabilities : bool
            If True, return class probabilities instead of labels
            
        Returns:
        --------
        predictions : pd.DataFrame
            Predictions for each horizon with columns:
            - actual_close
            - pred_1day, pred_3day, pred_5day, pred_10day (labels or probabilities)
            - cluster_id
        """
        if not self.is_fitted:
            raise ValueError("Model not fitted. Call fit() first.")
        
        # Calculate features
        features = self._calculate_features(data)
        
        # Create sequences
        X, y_dict, cluster_ids = self._create_sequences(features, include_cluster=True)
        
        # Scale
        n_sequences, lookback, n_features = X.shape
        X_reshaped = X.reshape(-1, n_features)
        X_scaled = self.scaler.transform(X_reshaped)
        X = X_scaled.reshape(n_sequences, lookback, n_features)
        
        # Predict
        predictions_raw = self.model.predict(X, verbose=0)
        
        # Create results dataframe
        start_idx = self.lookback_window
        results = pd.DataFrame(index=data.index[start_idx:start_idx + n_sequences])
        
        # Store actual close prices
        results['actual_close'] = data['Close'].iloc[start_idx:start_idx + n_sequences].values
        
        # Store cluster IDs
        results['cluster_id'] = cluster_ids
        
        # Process predictions for each horizon
        for i, horizon in enumerate(self.prediction_horizons):
            probs = predictions_raw[i]  # Shape: (n_sequences, 3)
            
            if return_probabilities:
                # Store probabilities for each class
                results[f'pred_{horizon}day_DOWN'] = probs[:, 0]
                results[f'pred_{horizon}day_FLAT'] = probs[:, 1]
                results[f'pred_{horizon}day_UP'] = probs[:, 2]
            
            # Store predicted class
            pred_labels = np.argmax(probs, axis=1)
            results[f'pred_{horizon}day'] = [self.classes[label] for label in pred_labels]
            
            # Store confidence (max probability)
            results[f'confidence_{horizon}day'] = np.max(probs, axis=1)
        
        return results
    
    def evaluate(self, data):
        """
        Evaluate model performance on test data.
        
        Parameters:
        -----------
        data : pd.DataFrame
            Test data
            
        Returns:
        --------
        metrics : dict
            Accuracy and confusion matrix for each horizon
        """
        if not self.is_fitted:
            raise ValueError("Model not fitted. Call fit() first.")
        
        # Get predictions
        predictions = self.predict(data, return_probabilities=True)
        
        # Calculate actual labels for each horizon
        features = self._calculate_features(data)
        
        metrics = {}
        
        for horizon in self.prediction_horizons:
            # Get actual labels
            actual_labels = self._create_labels(features, horizon)
            start_idx = self.lookback_window
            max_horizon = max(self.prediction_horizons)
            valid_actual = actual_labels[start_idx:start_idx + len(predictions)]
            
            # Get predicted labels
            pred_labels = predictions[f'pred_{horizon}day'].map({'DOWN': 0, 'FLAT': 1, 'UP': 2}).values
            
            # Calculate accuracy
            accuracy = (pred_labels == valid_actual).mean()
            
            # Confusion matrix
            from sklearn.metrics import confusion_matrix
            cm = confusion_matrix(valid_actual, pred_labels, labels=[0, 1, 2])
            
            metrics[horizon] = {
                'accuracy': accuracy,
                'confusion_matrix': cm,
                'n_samples': len(pred_labels)
            }
        
        return metrics, predictions
