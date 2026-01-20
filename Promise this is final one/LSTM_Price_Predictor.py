import numpy as np
import pandas as pd
from datetime import datetime
import os
import json
import warnings
warnings.filterwarnings('ignore')

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.preprocessing import StandardScaler


class LSTMPricePredictor:
    """
    LSTM-based price predictor for time series forecasting.
    Designed for computational efficiency and model persistence.
    """
    
    def __init__(self, 
                 lookback_window=100,
                 prediction_horizon=10,
                 lstm_units=50,
                 num_layers=2,
                 dropout=0.2,
                 epochs=50,
                 batch_size=32,
                 learning_rate=0.001,
                 prediction_mode='recursive',
                 model_dir='models',
                 verbose=1):
        """
        Parameters:
        -----------
        lookback_window : int
            Number of previous candles to use as input
        prediction_horizon : int
            Number of future candles to predict
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
        prediction_mode : str
            'recursive' or 'direct' prediction strategy
        model_dir : str
            Directory to save/load models
        verbose : int
            Verbosity level (0, 1, 2)
        """
        self.lookback_window = lookback_window
        self.prediction_horizon = prediction_horizon
        self.lstm_units = lstm_units
        self.num_layers = num_layers
        self.dropout = dropout
        self.epochs = epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.prediction_mode = prediction_mode
        self.model_dir = model_dir
        self.verbose = verbose
        
        self.model = None
        self.scaler = StandardScaler()
        self.is_fitted = False
        self.training_history = None
        self.feature_names = ['Open', 'High', 'Low', 'Close', 'Volume']
        
        # Create model directory if it doesn't exist
        os.makedirs(self.model_dir, exist_ok=True)
    
    def _compute_returns(self, data):
        """
        Efficiently compute percentage returns using vectorized operations.
        
        Parameters:
        -----------
        data : pd.DataFrame
            OHLCV data
            
        Returns:
        --------
        returns : np.ndarray
            Percentage returns for each feature
        """
        # Vectorized percentage change computation
        values = data[self.feature_names].values
        returns = np.zeros_like(values)
        returns[1:] = (values[1:] - values[:-1]) / values[:-1]
        returns[0] = 0  # First row has no previous data
        
        return returns
    
    def _create_sequences(self, returns, target_col_indices=[0, 1, 2, 3]):
        """
        Create input-output sequences for LSTM training.
        Optimized with NumPy for efficiency.
        Now predicts OHLC (4 values) instead of just Close.
        
        Parameters:
        -----------
        returns : np.ndarray
            Return data (n_samples, n_features)
        target_col_indices : list
            Indices of target columns [0=Open, 1=High, 2=Low, 3=Close]
            
        Returns:
        --------
        X : np.ndarray
            Input sequences (n_sequences, lookback_window, n_features)
        y : np.ndarray
            Target sequences (n_sequences, prediction_horizon, 4) for OHLC
        """
        n_samples = len(returns)
        n_features = returns.shape[1]
        
        # Calculate number of valid sequences
        n_sequences = n_samples - self.lookback_window - self.prediction_horizon + 1
        
        if n_sequences <= 0:
            raise ValueError(f"Not enough data. Need at least {self.lookback_window + self.prediction_horizon} samples.")
        
        # Pre-allocate arrays for efficiency
        X = np.zeros((n_sequences, self.lookback_window, n_features), dtype=np.float32)
        # y now has shape (n_sequences, prediction_horizon, 4) for OHLC
        y = np.zeros((n_sequences, self.prediction_horizon, 4), dtype=np.float32)
        
        # Vectorized sequence creation using advanced indexing
        for i in range(n_sequences):
            X[i] = returns[i:i + self.lookback_window]
            # Extract OHLC for all prediction steps
            y[i] = returns[i + self.lookback_window:i + self.lookback_window + self.prediction_horizon, target_col_indices]
        
        return X, y
    
    def _build_model(self, input_shape):
        """
        Build LSTM model architecture.
        
        Parameters:
        -----------
        input_shape : tuple
            (lookback_window, n_features)
        """
        model = Sequential(name='LSTM_Price_Predictor')
        
        # First LSTM layer
        model.add(LSTM(
            self.lstm_units,
            return_sequences=(self.num_layers > 1),
            input_shape=input_shape,
            name='lstm_1'
        ))
        model.add(Dropout(self.dropout, name='dropout_1'))
        
        # Additional LSTM layers
        for i in range(1, self.num_layers):
            return_seq = (i < self.num_layers - 1)
            model.add(LSTM(
                self.lstm_units,
                return_sequences=return_seq,
                name=f'lstm_{i+1}'
            ))
            model.add(Dropout(self.dropout, name=f'dropout_{i+1}'))
        
        # Output layer - now predicts 4 values (OHLC) per step
        if self.prediction_mode == 'direct':
            # Predict all N steps at once (N steps × 4 OHLC values)
            model.add(Dense(self.prediction_horizon * 4, name='output'))
        else:
            # Predict single step with 4 OHLC values (will be called recursively)
            model.add(Dense(4, name='output'))
        
        # Compile model
        model.compile(
            optimizer=Adam(learning_rate=self.learning_rate),
            loss='mse',
            metrics=['mae']
        )
        
        return model
    
    def fit(self, data, validation_split=0.2, early_stopping_patience=10):
        """
        Train the LSTM model on historical data.
        
        Parameters:
        -----------
        data : pd.DataFrame
            OHLCV data with columns: Open, High, Low, Close, Volume
        validation_split : float
            Fraction of data to use for validation
        early_stopping_patience : int
            Epochs to wait before early stopping
            
        Returns:
        --------
        self
        """
        if self.verbose:
            print(f"Computing returns from {len(data)} candles...")
        
        # Compute returns efficiently
        returns = self._compute_returns(data)
        
        # Scale returns for better training
        returns_scaled = self.scaler.fit_transform(returns)
        
        if self.verbose:
            print(f"Creating sequences (lookback={self.lookback_window}, horizon={self.prediction_horizon})...")
        
        # Create sequences
        X, y = self._create_sequences(returns_scaled)
        
        if self.verbose:
            print(f"Generated {len(X)} training sequences")
            print(f"Input shape: {X.shape}, Output shape: {y.shape}")
        
        # For recursive mode, we only train to predict 1 step ahead
        if self.prediction_mode == 'recursive':
            # y shape: (n_sequences, prediction_horizon, 4)
            # We want: (n_sequences, 4) for single-step OHLC prediction
            y = y[:, 0, :]  # Only first step, all 4 OHLC values
        
        # Build model
        if self.verbose:
            print("Building LSTM model...")
        
        self.model = self._build_model(input_shape=(self.lookback_window, X.shape[2]))
        
        if self.verbose:
            print(f"Model parameters: {self.model.count_params():,}")
        
        # Callbacks
        callbacks = [
            EarlyStopping(
                monitor='val_loss',
                patience=early_stopping_patience,
                restore_best_weights=True,
                verbose=self.verbose
            ),
            ModelCheckpoint(
                os.path.join(self.model_dir, 'best_model.keras'),
                monitor='val_loss',
                save_best_only=True,
                verbose=0
            )
        ]
        
        # Train model
        if self.verbose:
            print("Training model...")
        
        self.training_history = self.model.fit(
            X, y,
            epochs=self.epochs,
            batch_size=self.batch_size,
            validation_split=validation_split,
            callbacks=callbacks,
            verbose=self.verbose
        )
        
        self.is_fitted = True
        
        if self.verbose:
            final_loss = self.training_history.history['loss'][-1]
            final_val_loss = self.training_history.history['val_loss'][-1]
            print(f"Training complete! Final loss: {final_loss:.6f}, Val loss: {final_val_loss:.6f}")
        
        return self
    
    def _predict_recursive(self, initial_sequence):
        """
        Recursively predict N steps ahead.
        Each prediction feeds into the next.
        Now predicts full OHLC candles instead of just Close.
        
        Parameters:
        -----------
        initial_sequence : np.ndarray
            Starting sequence (lookback_window, n_features)
            
        Returns:
        --------
        predictions : np.ndarray
            Predicted OHLC returns for N steps (prediction_horizon, 4)
        """
        current_sequence = initial_sequence.copy()
        predictions = np.zeros((self.prediction_horizon, 4), dtype=np.float32)
        
        for step in range(self.prediction_horizon):
            # Predict next step (returns 4 values: OHLC)
            next_pred = self.model.predict(
                current_sequence[np.newaxis, :, :],
                verbose=0
            )[0]  # Shape: (4,) for OHLC
            
            predictions[step] = next_pred
            
            # Update sequence: shift left and append predicted OHLC
            new_row = np.zeros(current_sequence.shape[1], dtype=np.float32)
            new_row[0:4] = next_pred  # OHLC predictions
            # For Volume, use simple persistence (last value)
            new_row[4] = current_sequence[-1, 4]
            
            current_sequence = np.vstack([current_sequence[1:], new_row])
        
        return predictions
    
    def _batch_predict_recursive(self, sequences, batch_size=32):
        """
        Batch version of recursive prediction for multiple sequences.
        Processes predictions in batches for efficiency.
        Now handles OHLC predictions (4 values per step).
        
        Parameters:
        -----------
        sequences : np.ndarray
            Multiple starting sequences (n_sequences, lookback_window, n_features)
        batch_size : int
            Batch size for predictions
            
        Returns:
        --------
        all_predictions : np.ndarray
            Predicted OHLC returns for all sequences (n_sequences, prediction_horizon, 4)
        """
        n_sequences = len(sequences)
        all_predictions = np.zeros((n_sequences, self.prediction_horizon, 4), dtype=np.float32)
        
        # Process each prediction step across all sequences
        current_sequences = sequences.copy()
        
        for step in range(self.prediction_horizon):
            # Batch predict for all sequences at this step
            step_predictions = self.model.predict(
                current_sequences,
                batch_size=batch_size,
                verbose=0
            )  # Shape: (n_sequences, 4) for OHLC
            
            all_predictions[:, step, :] = step_predictions
            
            # Update all sequences for next step
            if step < self.prediction_horizon - 1:  # Don't update on last step
                for i in range(n_sequences):
                    new_row = np.zeros(current_sequences.shape[2], dtype=np.float32)
                    new_row[0:4] = step_predictions[i]  # OHLC predictions
                    new_row[4] = current_sequences[i, -1, 4]  # Volume persistence
                    
                    # Shift sequence and append new prediction
                    current_sequences[i] = np.vstack([current_sequences[i, 1:], new_row])
        
        return all_predictions
    
    def _predict_direct(self, sequence):
        """
        Directly predict all N steps at once.
        Now handles OHLC predictions (4 values per step).
        
        Parameters:
        -----------
        sequence : np.ndarray
            Input sequence (lookback_window, n_features)
            
        Returns:
        --------
        predictions : np.ndarray
            Predicted OHLC returns for N steps (prediction_horizon, 4)
        """
        predictions = self.model.predict(
            sequence[np.newaxis, :, :],
            verbose=0
        )[0]  # Shape: (prediction_horizon * 4,)
        
        # Reshape to (prediction_horizon, 4)
        predictions = predictions.reshape(self.prediction_horizon, 4)
        
        return predictions
    
    def predict(self, data, start_idx=None):
        """
        Generate predictions on new data.
        
        Parameters:
        -----------
        data : pd.DataFrame
            OHLCV data
        start_idx : int, optional
            Index to start predictions from. If None, predicts for all valid positions.
            
        Returns:
        --------
        predictions_df : pd.DataFrame
            DataFrame with columns for each prediction step and actual prices
        """
        if not self.is_fitted:
            raise ValueError("Model must be fitted before prediction. Call .fit() first.")
        
        # Compute returns
        returns = self._compute_returns(data)
        returns_scaled = self.scaler.transform(returns)
        
        # Determine prediction range
        if start_idx is None:
            start_idx = self.lookback_window
        
        end_idx = len(data) - self.prediction_horizon
        
        if start_idx >= end_idx:
            raise ValueError(f"Not enough data for predictions. Need at least {self.lookback_window + self.prediction_horizon} samples.")
        
        n_predictions = end_idx - start_idx + 1
        
        if self.verbose:
            print(f"Generating {n_predictions} predictions in batched mode...")
        
        # Create all sequences at once (vectorized operation)
        all_sequences = np.zeros((n_predictions, self.lookback_window, returns_scaled.shape[1]), dtype=np.float32)
        for i, idx in enumerate(range(start_idx, end_idx + 1)):
            all_sequences[i] = returns_scaled[idx - self.lookback_window:idx]
        
        # Batch predictions based on mode
        if self.prediction_mode == 'recursive':
            # Batch recursive prediction (processes all sequences together by step)
            all_predictions = self._batch_predict_recursive(all_sequences, batch_size=self.batch_size)
        else:
            # Direct mode: predict all at once
            raw_predictions = self.model.predict(
                all_sequences,
                batch_size=self.batch_size,
                verbose=0 if not self.verbose else 1
            )  # Shape: (n_predictions, prediction_horizon * 4)
            # Reshape to (n_predictions, prediction_horizon, 4)
            all_predictions = raw_predictions.reshape(n_predictions, self.prediction_horizon, 4)
        
        if self.verbose:
            print(f"Predictions complete!")
        
        # Convert returns back to prices
        results = self._returns_to_prices(data, all_predictions, start_idx)
        
        return results
    
    def _returns_to_prices(self, data, predicted_returns, start_idx):
        """
        Convert predicted OHLC returns back to actual OHLC price predictions.
        
        Parameters:
        -----------
        data : pd.DataFrame
            Original OHLCV data
        predicted_returns : np.ndarray
            Predicted OHLC returns (n_predictions, prediction_horizon, 4)
        start_idx : int
            Starting index for predictions
            
        Returns:
        --------
        results : pd.DataFrame
            DataFrame with actual OHLC and predicted OHLC prices
        """
        ohlc_data = data[['Open', 'High', 'Low', 'Close']].values
        n_predictions = len(predicted_returns)
        
        results = pd.DataFrame(index=data.index[start_idx:start_idx + n_predictions])
        # Store actual OHLC
        results['actual_open'] = ohlc_data[start_idx:start_idx + n_predictions, 0]
        results['actual_high'] = ohlc_data[start_idx:start_idx + n_predictions, 1]
        results['actual_low'] = ohlc_data[start_idx:start_idx + n_predictions, 2]
        results['actual_close'] = ohlc_data[start_idx:start_idx + n_predictions, 3]
        # Keep backward compatibility
        results['actual_price'] = results['actual_close']
        
        # Convert each prediction horizon to actual OHLC prices
        for step in range(self.prediction_horizon):
            pred_open = np.zeros(n_predictions, dtype=np.float32)
            pred_high = np.zeros(n_predictions, dtype=np.float32)
            pred_low = np.zeros(n_predictions, dtype=np.float32)
            pred_close = np.zeros(n_predictions, dtype=np.float32)
            
            for i in range(n_predictions):
                # Base prices from previous candle
                base_open = ohlc_data[start_idx + i - 1, 0]
                base_high = ohlc_data[start_idx + i - 1, 1]
                base_low = ohlc_data[start_idx + i - 1, 2]
                base_close = ohlc_data[start_idx + i - 1, 3]
                
                # Compound returns for multi-step predictions (OHLC separately)
                cumulative_returns = np.ones(4, dtype=np.float32)
                for s in range(step + 1):
                    cumulative_returns *= (1 + predicted_returns[i, s, :])
                
                pred_open[i] = base_open * cumulative_returns[0]
                pred_high[i] = base_high * cumulative_returns[1]
                pred_low[i] = base_low * cumulative_returns[2]
                pred_close[i] = base_close * cumulative_returns[3]
            
            # Store predicted OHLC for this horizon
            results[f'pred_open_{step+1}'] = pred_open
            results[f'pred_high_{step+1}'] = pred_high
            results[f'pred_low_{step+1}'] = pred_low
            results[f'pred_close_{step+1}'] = pred_close
            # Keep backward compatibility
            results[f'pred_price_{step+1}'] = pred_close
        
        return results
    
    def save_model(self, model_name):
        """
        Save trained model and metadata.
        
        Parameters:
        -----------
        model_name : str
            Name for the saved model
        """
        if not self.is_fitted:
            raise ValueError("No trained model to save.")
        
        model_path = os.path.join(self.model_dir, f"{model_name}.keras")
        metadata_path = os.path.join(self.model_dir, f"{model_name}_metadata.json")
        scaler_path = os.path.join(self.model_dir, f"{model_name}_scaler.npz")
        
        # Save model
        self.model.save(model_path)
        
        # Save metadata
        metadata = {
            'lookback_window': self.lookback_window,
            'prediction_horizon': self.prediction_horizon,
            'lstm_units': self.lstm_units,
            'num_layers': self.num_layers,
            'dropout': self.dropout,
            'prediction_mode': self.prediction_mode,
            'feature_names': self.feature_names,
            'training_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'final_train_loss': float(self.training_history.history['loss'][-1]),
            'final_val_loss': float(self.training_history.history['val_loss'][-1])
        }
        
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        
        # Save scaler
        np.savez(scaler_path,
                 mean=self.scaler.mean_,
                 scale=self.scaler.scale_)
        
        print(f"Model saved to {model_path}")
        print(f"Metadata saved to {metadata_path}")
    
    def load_model(self, model_name):
        """
        Load a previously trained model.
        
        Parameters:
        -----------
        model_name : str
            Name of the saved model
            
        Returns:
        --------
        self
        """
        model_path = os.path.join(self.model_dir, f"{model_name}.keras")
        metadata_path = os.path.join(self.model_dir, f"{model_name}_metadata.json")
        scaler_path = os.path.join(self.model_dir, f"{model_name}_scaler.npz")
        
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found: {model_path}")
        
        # Load model
        self.model = load_model(model_path)
        
        # Load metadata
        with open(metadata_path, 'r') as f:
            metadata = json.load(f)
        
        # Restore parameters
        self.lookback_window = metadata['lookback_window']
        self.prediction_horizon = metadata['prediction_horizon']
        self.lstm_units = metadata['lstm_units']
        self.num_layers = metadata['num_layers']
        self.dropout = metadata['dropout']
        self.prediction_mode = metadata['prediction_mode']
        self.feature_names = metadata['feature_names']
        
        # Load scaler
        scaler_data = np.load(scaler_path)
        self.scaler.mean_ = scaler_data['mean']
        self.scaler.scale_ = scaler_data['scale']
        
        self.is_fitted = True
        
        print(f"Model loaded from {model_path}")
        print(f"Trained on: {metadata['training_date']}")
        print(f"Training loss: {metadata['final_train_loss']:.6f}")
        
        return self
    
    def get_training_history(self):
        """
        Get training history for visualization.
        
        Returns:
        --------
        history_df : pd.DataFrame
            Training metrics by epoch
        """
        if self.training_history is None:
            raise ValueError("No training history available. Train the model first.")
        
        history_df = pd.DataFrame(self.training_history.history)
        history_df['epoch'] = range(1, len(history_df) + 1)
        
        return history_df
    
    def evaluate(self, data=None, tolerance_levels=[0.001, 0.005, 0.01], predictions=None):
        """
        Evaluate model performance on data with comprehensive trading metrics.
        
        Parameters:
        -----------
        data : pd.DataFrame, optional
            OHLCV data for evaluation (not needed if predictions provided)
        tolerance_levels : list of float
            Tolerance thresholds for hit rate calculation (e.g., 0.001 = 0.1%)
        predictions : pd.DataFrame, optional
            Pre-computed predictions DataFrame. If provided, skips prediction step.
            
        Returns:
        --------
        metrics : pd.DataFrame
            Performance metrics including MAE, RMSE, MAPE, directional accuracy, and hit rates
        """
        if predictions is None:
            if data is None:
                raise ValueError("Must provide either 'data' or 'predictions'")
            predictions = self.predict(data)
        
        metrics = {}
        
        for step in range(1, self.prediction_horizon + 1):
            actual = predictions['actual_price'].values
            pred = predictions[f'pred_price_{step}'].values
            
            # Value-based metrics
            mae = np.mean(np.abs(actual - pred))
            rmse = np.sqrt(np.mean((actual - pred) ** 2))
            mape = np.mean(np.abs((actual - pred) / actual)) * 100
            
            # Directional accuracy (did we predict up/down correctly?)
            if len(actual) > 1:
                actual_direction = np.sign(np.diff(actual))
                pred_direction = np.sign(pred[1:] - actual[:-1])
                direction_accuracy = np.mean(actual_direction == pred_direction) * 100
            else:
                direction_accuracy = np.nan
            
            # Hit rates at different tolerance levels
            hit_rates = {}
            for tolerance in tolerance_levels:
                pct_error = np.abs((pred - actual) / actual)
                hit_rate = np.mean(pct_error <= tolerance) * 100
                hit_rates[f'Hit_Rate_{tolerance*100:.1f}%'] = hit_rate
            
            metrics[f'step_{step}'] = {
                'MAE': mae,
                'RMSE': rmse,
                'MAPE': mape,
                'Direction_Accuracy': direction_accuracy,
                **hit_rates
            }
        
        return pd.DataFrame(metrics).T
    
    def get_directional_accuracy(self, data=None, detailed=False, predictions=None):
        """
        Calculate detailed directional accuracy metrics.
        
        Parameters:
        -----------
        data : pd.DataFrame, optional
            OHLCV data for evaluation (not needed if predictions provided)
        detailed : bool
            If True, returns detailed breakdown (true positives, false positives, etc.)
        predictions : pd.DataFrame, optional
            Pre-computed predictions DataFrame. If provided, skips prediction step.
            
        Returns:
        --------
        results : pd.DataFrame or dict
            Directional accuracy metrics by prediction step
        """
        if predictions is None:
            if data is None:
                raise ValueError("Must provide either 'data' or 'predictions'")
            predictions = self.predict(data)
        actual = predictions['actual_price'].values
        
        if len(actual) <= 1:
            raise ValueError("Need at least 2 data points for directional accuracy")
        
        # Actual direction changes
        actual_direction = np.sign(np.diff(actual))
        
        results = {}
        
        for step in range(1, self.prediction_horizon + 1):
            pred = predictions[f'pred_price_{step}'].values
            pred_direction = np.sign(pred[1:] - actual[:-1])
            
            # Overall accuracy
            correct = actual_direction == pred_direction
            accuracy = np.mean(correct) * 100
            
            if detailed:
                # Breakdown by direction
                up_mask = actual_direction > 0
                down_mask = actual_direction < 0
                flat_mask = actual_direction == 0
                
                pred_up_mask = pred_direction > 0
                pred_down_mask = pred_direction < 0
                
                # True positives / negatives
                true_up = np.sum(up_mask & pred_up_mask)
                true_down = np.sum(down_mask & pred_down_mask)
                false_up = np.sum(down_mask & pred_up_mask)  # Predicted up, actually down
                false_down = np.sum(up_mask & pred_down_mask)  # Predicted down, actually up
                
                total_up = np.sum(up_mask)
                total_down = np.sum(down_mask)
                
                results[f'step_{step}'] = {
                    'Accuracy': accuracy,
                    'Total_Predictions': len(correct),
                    'Correct': np.sum(correct),
                    'Incorrect': np.sum(~correct),
                    'Actual_Up_Days': total_up,
                    'Actual_Down_Days': total_down,
                    'Actual_Flat_Days': np.sum(flat_mask),
                    'True_Up': true_up,
                    'True_Down': true_down,
                    'False_Up': false_up,
                    'False_Down': false_down,
                    'Up_Accuracy': (true_up / total_up * 100) if total_up > 0 else np.nan,
                    'Down_Accuracy': (true_down / total_down * 100) if total_down > 0 else np.nan
                }
            else:
                results[f'step_{step}'] = {'Accuracy': accuracy}
        
        return pd.DataFrame(results).T
    
    def get_hit_rates(self, data=None, tolerance_levels=[0.001, 0.005, 0.01, 0.02], predictions=None):
        """
        Calculate hit rates at multiple tolerance levels ("close enough" accuracy).
        
        Parameters:
        -----------
        data : pd.DataFrame, optional
            OHLCV data for evaluation (not needed if predictions provided)
        tolerance_levels : list of float
            Tolerance thresholds (e.g., 0.001 = 0.1%, 0.01 = 1%)
        predictions : pd.DataFrame, optional
            Pre-computed predictions DataFrame. If provided, skips prediction step.
            
        Returns:
        --------
        results : pd.DataFrame
            Hit rates for each prediction step at each tolerance level
        """
        if predictions is None:
            if data is None:
                raise ValueError("Must provide either 'data' or 'predictions'")
            predictions = self.predict(data)
        actual = predictions['actual_price'].values
        
        results = {}
        
        for step in range(1, self.prediction_horizon + 1):
            pred = predictions[f'pred_price_{step}'].values
            
            step_results = {}
            for tolerance in tolerance_levels:
                pct_error = np.abs((pred - actual) / actual)
                hits = pct_error <= tolerance
                
                hit_rate = np.mean(hits) * 100
                hit_count = np.sum(hits)
                miss_count = np.sum(~hits)
                
                tolerance_pct = tolerance * 100
                step_results[f'±{tolerance_pct:.1f}%_HitRate'] = hit_rate
                step_results[f'±{tolerance_pct:.1f}%_Hits'] = hit_count
                step_results[f'±{tolerance_pct:.1f}%_Misses'] = miss_count
            
            results[f'step_{step}'] = step_results
        
        return pd.DataFrame(results).T
