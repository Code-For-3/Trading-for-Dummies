import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_ta as ta
import yfinance as yf
#import alpaca_trade_api as tradeapi
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from datetime import datetime
import pandas as pd
import numpy as np
from scipy.stats import linregress
from mplfinance.original_flavor import candlestick_ohlc


#import plotly # for interactive plots
#import backtesting.py or bt or vectorbt #might not work with pandas-ta






# Section 1: Imports ========================================================================================================== Section 1: Imports


# Alpaca API Credentials
API_KEY = "PKP6G2PCSLR7KABZBU9Z"
API_SECRET = "mPNf9KoilrmoMdz4MedQdeaZWxda3D1YjgCIJbjd"

client = StockHistoricalDataClient(API_KEY, API_SECRET)

# Supported Timeframe
SUPPORTED_TIMEFRAMES = {
    "Minute": [1, 5, 15],
    "Hour": [1],
    "Day": [1]
}

# ==========================
# Fetching Stock Data
# ==========================

def get_stock_data(symbol: str, start_date: str, end_date: str,
                   timeframe_unit: str = "Day", multiplier: int = 1):
                   
    if timeframe_unit not in SUPPORTED_TIMEFRAMES:
        raise ValueError(f"Unsupported timeframe unit: {timeframe_unit}")
    if multiplier not in SUPPORTED_TIMEFRAMES[timeframe_unit]:
        raise ValueError(f"Unsupported multiplier '{multiplier}' for '{timeframe_unit}'")

    unit_enum = TimeFrameUnit[timeframe_unit]
    alpaca_timeframe = TimeFrame(multiplier, unit_enum)

    request_params = StockBarsRequest(
        symbol_or_symbols=[symbol],
        timeframe=alpaca_timeframe,
        start=datetime.strptime(start_date, "%Y-%m-%d"),
        end=datetime.strptime(end_date, "%Y-%m-%d")
    )

    bars = client.get_stock_bars(request_params)
    df = bars.df

    # Handle both flat and MultiIndex column cases
    if isinstance(df.columns, pd.MultiIndex):
        if symbol in df.columns.levels[0]:
            df = df.xs(symbol, axis=1, level=0)
        else:
            raise KeyError(f"Symbol '{symbol}' not found in returned data columns.")
    
    # Check for required columns and raise helpful error if missing
    required_cols = ['open', 'high', 'low', 'close', 'volume']
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        raise KeyError(f"Missing columns in data: {missing}\nAvailable columns: {df.columns.tolist()}")

    # Clean non-trading days
    df = df.dropna(subset=['open', 'high', 'low', 'close', 'volume'])

    # Drop fake/no-trade rows
    df = df[~(
        (df['open'] == df['high']) &
        (df['high'] == df['low']) &
        (df['low'] == df['close']) &
        (df['volume'] == 0)
    )]

    return df[required_cols]

# ==========================
# Extracting Close and Volume
# ==========================

def extract_close_volume(df, required_cols = ['close', 'volume']):
    return df[required_cols].copy()




# Section 2: Plots ========================================================================================================== Section 2: Plots


# ==========================
# Plotting Candlestick with Volume
# ==========================

def plot_candlestick_with_volume(df, symbol: str):
    # If MultiIndex (e.g., (symbol, datetime)), reduce to datetime index
    if isinstance(df.index, pd.MultiIndex):
        df = df.reset_index(level=0, drop=True)

    # Ensure index is datetime
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)

    # Reset index for plotting
    df_plot = df.copy().reset_index()
    df_plot.rename(columns={df_plot.columns[0]: 'timestamp'}, inplace=True)

    # Use integer x positions (0, 1, 2, ...) to enforce uniform spacing
    df_plot['x'] = range(len(df_plot))

    # Build OHLC data
    quotes = list(zip(
        df_plot['x'],
        df_plot['open'],
        df_plot['high'],
        df_plot['low'],
        df_plot['close']
    ))

    # Plot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 9), sharex=True,
                                   gridspec_kw={'height_ratios': [3, 1]})

    candlestick_ohlc(ax1, quotes, width=0.6, colorup='g', colordown='r', alpha=0.7)
    ax1.set_title(f'{symbol} Candlestick Chart')
    ax1.set_ylabel('Price')
    ax1.grid(True)

    # Volume bars

    # Determine color based on price direction
    volume_colors = np.where(df_plot['close'] >= df_plot['open'], 'green', 'red')

    # Volume bars without gaps between them
    ax2.bar(df_plot['x'], df_plot['volume'], color=volume_colors, width=1.0, alpha=0.6)
    ax2.set_ylabel('Volume')
    ax2.grid(True)

    # Set x-ticks to timestamps
    tick_interval = max(1, len(df_plot) // 10)
    ax2.set_xticks(df_plot['x'][::tick_interval])
    ax2.set_xticklabels(df_plot['timestamp'].dt.strftime('%Y-%m-%d')[::tick_interval], rotation=45)

    plt.tight_layout()
    plt.show()


# ==========================
# Plotting Strategy Signals over price
# ==========================

def plot_price_with_signals(df, indicators=None):
    if isinstance(df.index, pd.MultiIndex):
        df = df.copy()
        df.index = df.index.get_level_values(-1)
        
    if 'close' not in df.columns:
        raise KeyError("'close' column is required in the DataFrame.")
    
    if indicators is None:
        indicators = []

    # Check for missing indicators
    for col in indicators:
        if col not in df.columns:
            raise KeyError(f"Indicator '{col}' is missing from DataFrame.")

    fig, ax = plt.subplots(figsize=(14, 6))

    # Plot close price with light blue fill
    ax.plot(df.index, df['close'], label='Close Price', color='tab:blue', linewidth=1.5)
    ax.fill_between(df.index, df['close'], color='tab:blue', alpha=0.2)

    # Highlight full chart background using axvspan
    if 'signal' in df.columns:
        current_signal = 0
        start_time = None

        for i in range(len(df)):
            signal = df['signal'].iloc[i]
            time = df.index[i]

            if signal != current_signal:
                # End previous region
                if current_signal == 1:
                    ax.axvspan(start_time, time, color='green', alpha=0.2)
                elif current_signal == -1:
                    ax.axvspan(start_time, time, color='red', alpha=0.2)

                # Start new region
                current_signal = signal
                start_time = time

        # Finish last region
        if current_signal == 1:
            ax.axvspan(start_time, df.index[-1], color='green', alpha=0.2)
        elif current_signal == -1:
            ax.axvspan(start_time, df.index[-1], color='red', alpha=0.2)

    # Plot additional indicators
    for col in indicators:
        ax.plot(df.index, df[col], label=col, linestyle='--')

    ax.set_title("Close Price with Signal Highlights")
    ax.set_ylabel("Price")
    ax.set_xlabel("Time")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    plt.show()


# =========================
# Plotting Individual Strategies
# =========================





# Section 3: Strategies ========================================================================================================== Section 3: Strategies

# =========================
# Strategy Base Class
# =========================
# This is a base class for all strategies. Each strategy should inherit from this class and implement the generate_signal method.
# The generate_signal method should take a DataFrame as input and return a DataFrame with a 'signal' column.

class Strategy:
    def generate_signal(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply strategy logic and return DataFrame with a 'signal' column"""
        raise NotImplementedError("Subclasses must implement generate_signal()")


# =========================
# Moving Average Crossover Strategy
# =========================

                class MovingAverageCrossoverStrategy(Strategy):
                    def __init__(self, short_window=50, long_window=200, signal_col='signal_ma'):
                        self.short_window = short_window
                        self.long_window = long_window
                        self.signal_col = signal_col

                    def generate_signal(self, df: pd.DataFrame) -> pd.DataFrame:
                        # Compute moving averages only if missing
                        if f"SMA_{self.short_window}" not in df.columns:
                            df[f"SMA_{self.short_window}"] = ta.sma(df['close'], length=self.short_window)
                        if f"SMA_{self.long_window}" not in df.columns:
                            df[f"SMA_{self.long_window}"] = ta.sma(df['close'], length=self.long_window)

                        short_ma = df[f"SMA_{self.short_window}"]
                        long_ma = df[f"SMA_{self.long_window}"]

                        df[self.signal_col] = np.where(short_ma > long_ma, 1,
                                                np.where(short_ma < long_ma, -1, 0))
                        return df
    
# =========================
# RSI Strategy
# =========================

class RSIStrategy(Strategy):
    def __init__(self, length=14, overbought=70, oversold=30"):
        self.length = length
        self.overbought = overbought
        self.oversold = oversold
        self.signal_col = signal_col
        self.indicator_col = f"RSI_{self.length}"

    def generate_signal(self, df: pd.DataFrame) -> pd.DataFrame:
        # Compute RSI only if missing
        if self.indicator_col not in df.columns:
            df[self.indicator_col] = ta.rsi(df['close'], length=self.length)

        rsi = df[self.indicator_col]
        df[self.signal_col] = np.where(rsi > self.overbought, -1,
                                np.where(rsi < self.oversold, 1, 0))
        return df






