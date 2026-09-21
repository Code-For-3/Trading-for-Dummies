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
from matplotlib.ticker import FixedLocator


#import plotly # for interactive plots
#import backtesting.py or bt or vectorbt #might not work with pandas-ta






# Section 1: Imports ========================================================================================================== Section 1: Imports & Data Formatting


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

def get_stock_data(symbol: str, start_date: str, end_date: str, timeframe_unit: str = "Day", multiplier: int = 1):
                   
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

def remove_hol(df):
    cols_to_drop = [col for col in ['open', 'high', 'low'] if col in df.columns]
    return df.drop(columns=cols_to_drop)



# Section 2: Plots ========================================================================================================== Section 2: Plots


# ==========================
# Plotting Candlestick with Volume
# ==========================

def plot_candlestick_with_volume(df, symbol: str = None, use_log_volume=False, clip_volume=True):
    # Handle MultiIndex (e.g., symbol, datetime)
    if isinstance(df.index, pd.MultiIndex):
        df = df.reset_index(level=0, drop=True)

    # Ensure datetime index
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)

    # Reset index for plotting
    df_plot = df.copy().reset_index()
    df_plot.rename(columns={df_plot.columns[0]: 'timestamp'}, inplace=True)
    df_plot['x'] = range(len(df_plot))

    # Auto-extract symbol if not given
    if symbol is None:
        if 'symbol' in df.columns:
            symbol = df['symbol'].iloc[0]
        else:
            symbol = "Unknown"

    # Candlestick OHLC tuples
    quotes = list(zip(
        df_plot['x'],
        df_plot['open'],
        df_plot['high'],
        df_plot['low'],
        df_plot['close']
    ))

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 9), sharex=True,
                                   gridspec_kw={'height_ratios': [3, 1]})

    # Plot candlestick chart
    candlestick_ohlc(ax1, quotes, width=0.6, colorup='g', colordown='r', alpha=0.7)
    ax1.set_title(f'{symbol} Candlestick Chart')
    ax1.set_ylabel('Price')
    ax1.grid(True)

    # Volume colors based on candle direction
    volume_colors = np.where(df_plot['close'] >= df_plot['open'], 'green', 'red')

    # Clip volume to 99th percentile if enabled
    if clip_volume:
        volume_cap = np.percentile(df_plot['volume'], 99)
        df_plot['volume_to_plot'] = np.minimum(df_plot['volume'], volume_cap)
    else:
        df_plot['volume_to_plot'] = df_plot['volume']

    # Plot volume bars
    ax2.bar(df_plot['x'], df_plot['volume_to_plot'], color=volume_colors, width=0.6, alpha=0.6)
    ax2.set_ylabel('Volume')
    ax2.grid(True)

    # Optional log scale
    if use_log_volume:
        ax2.set_yscale('log')

    # Format x-axis ticks with readable dates
    tick_interval = max(1, len(df_plot) // 10)
    x_ticks = df_plot['x'][::tick_interval]
    x_labels = df_plot['timestamp'].dt.strftime('%Y-%m-%d').iloc[::tick_interval]
    ax2.xaxis.set_major_locator(FixedLocator(x_ticks))
    ax2.set_xticklabels(x_labels, rotation=45, ha='right')

    fig.subplots_adjust(bottom=0.2)
    plt.tight_layout()
    plt.show()






# =========================
# Plotting Individual Strategies ##### come back to later, i actually dont care about visual representation of strategies so much
# =========================





# Section 3: Strategies ========================================================================================================== Section 3: Strategies

# =========================
# Strategy Base Class
# =========================
# This is a base class for all strategies. Each strategy should inherit from this class and implement the generate_signal method.
# The generate_signal method should take a DataFrame as input and return a DataFrame with a 'signal' column.

class Strategy:
    def __init__(self):
        self.signal_col: str = None
        self.compute: bool = True

    def plot_price_with_signals(self, df: pd.DataFrame):
        if isinstance(df.index, pd.MultiIndex):
            df = df.copy()
            df.index = df.index.get_level_values(-1)

        if "close" not in df.columns:
            raise KeyError(f"'close' column is required in the DataFrame.")

        # If compute is False, force signal generation
        if not self.compute:
            df = self.generate_signal(df)

        # If signal_col is not set, treat as "no strategy" plot — flat signal
        if not self.signal_col:
            self.signal_col = '__flat_signal__'
            df[self.signal_col] = 0  # flat signal, no action

        # Prepare data for plotting
        df_plot = df.copy().reset_index()
        df_plot.rename(columns={df_plot.columns[0]: 'timestamp'}, inplace=True)
        df_plot['x'] = range(len(df_plot))

        fig, ax = plt.subplots(figsize=(14, 6))
        ax.plot(df_plot['x'], df_plot['close'], label='Close', color='tab:blue', linewidth=1.5)
        ax.fill_between(df_plot['x'], df_plot['close'], color='tab:blue', alpha=0.2)

        # Plot shaded signal regions
        current_signal = 0
        start_idx = 0
        for i in range(len(df_plot)):
            signal = df[self.signal_col].iloc[i]
            if signal != current_signal:
                if current_signal == 1:
                    ax.axvspan(start_idx, i, color='green', alpha=0.2)
                elif current_signal == -1:
                    ax.axvspan(start_idx, i, color='red', alpha=0.2)
                current_signal = signal
                start_idx = i

        # Final region to the end
        if current_signal == 1:
            ax.axvspan(start_idx, len(df_plot) - 1, color='green', alpha=0.2)
        elif current_signal == -1:
            ax.axvspan(start_idx, len(df_plot) - 1, color='red', alpha=0.2)

        # Dynamic y-axis scaling
        ymin = df_plot['close'].min()
        ymax = df_plot['close'].max()
        padding = (ymax - ymin) * 0.02
        ax.set_ylim(ymin - padding, ymax + padding)

        # Format X-axis ticks with readable timestamps
        tick_interval = max(1, len(df_plot) // 8)
        x_ticks = df_plot['x'][::tick_interval]
        x_labels = df_plot['timestamp'].dt.strftime('%Y-%m-%d').iloc[::tick_interval]
        ax.xaxis.set_major_locator(FixedLocator(x_ticks))
        ax.set_xticklabels(x_labels, rotation=45, ha='right')

        ax.set_title(f"Close with {self.signal_col} Highlights")
        ax.set_ylabel("Price")
        ax.set_xlabel("Time")
        ax.grid(True)
        ax.legend()
        fig.subplots_adjust(bottom=0.2)
        plt.tight_layout()
        plt.show()


    def generate_signal(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply strategy logic and return DataFrame with a 'signal' column"""
        raise NotImplementedError("Subclasses must implement generate_signal()")
    
    def plot_trades(self, df: pd.DataFrame):
        if isinstance(df.index, pd.MultiIndex):
            df = df.copy()
            df.index = df.index.get_level_values(-1)

        if 'close' not in df.columns:
            raise KeyError(f"'{'close'}' column is required in the DataFrame.")

        if not self.compute:
            df = self.generate_signal(df)

        if not self.signal_col:
            self.signal_col = '__flat_signal__'
            df[self.signal_col] = 0

        signal = df[self.signal_col]
        price = df['close']

        has_ohlc = all(col in df.columns for col in ['open', 'high', 'low', 'close', 'volume'])

        df_plot = df.copy().reset_index()
        df_plot.rename(columns={df_plot.columns[0]: 'timestamp'}, inplace=True)
        df_plot['x'] = range(len(df_plot))

        fig, ax = plt.subplots(figsize=(14, 6))

        if has_ohlc:
            quotes = list(zip(
                df_plot['x'],
                df_plot['open'],
                df_plot['high'],
                df_plot['low'],
                df_plot['close']
            ))
            candlestick_ohlc(ax, quotes, width=0.6, colorup='g', colordown='r', alpha=0.7)
        else:
            ax.plot(df_plot['x'], df_plot['close'], label='Price', color='tab:blue', linewidth=1.5)

        # Trade markers
        in_trade = False
        entry_idx = None
        entry_price = None
        direction = None

        for i in range(1, len(signal)):
            curr_sig = signal.iloc[i]
            x = df_plot['x'].iloc[i]
            p = df_plot['close'].iloc[i]

            # ENTRY LONG
            if not in_trade and curr_sig == 1:
                entry_idx = x
                entry_price = p
                direction = 'long'
                in_trade = True
                ax.plot(x, p, marker='^', color='green', markersize=10)

            # ENTRY SHORT
            elif not in_trade and curr_sig == -1:
                entry_idx = x
                entry_price = p
                direction = 'short'
                in_trade = True
                ax.plot(x, p, marker='v', color='red', markersize=10)

            # EXIT LONG
            elif in_trade and direction == 'long' and curr_sig != 1:
                ax.plot(x, p, marker='x', color='black', markersize=10)
                color = 'green' if p > entry_price else 'red'
                ax.plot([entry_idx, x], [entry_price, p], linestyle='--', linewidth=2.5, color=color)
                in_trade = False

            # EXIT SHORT
            elif in_trade and direction == 'short' and curr_sig != -1:
                ax.plot(x, p, marker='x', color='black', markersize=10)
                color = 'green' if p < entry_price else 'red'
                ax.plot([entry_idx, x], [entry_price, p], linestyle='--', linewidth=2.5, color=color)
                in_trade = False

        # Y-axis zoom
        ymin = df_plot['close'].min()
        ymax = df_plot['close'].max()
        padding = (ymax - ymin) * 0.02
        ax.set_ylim(ymin - padding, ymax + padding)

        # X-axis formatting
        tick_interval = max(1, len(df_plot) // 8)
        x_ticks = df_plot['x'][::tick_interval]
        x_labels = df_plot['timestamp'].dt.strftime('%Y-%m-%d').iloc[::tick_interval]
        ax.xaxis.set_major_locator(FixedLocator(x_ticks))
        ax.set_xticklabels(x_labels, rotation=45, ha='right')

        ax.set_title(f"Trade Entries & Exits ({self.signal_col})")
        ax.set_ylabel("Price")
        ax.set_xlabel("Time")
        ax.grid(True)
        fig.subplots_adjust(bottom=0.2)
        plt.tight_layout()
        plt.show()







# =========================
# Moving Average Crossover Strategy
# =========================

class SMACrossoverStrategy(Strategy):
    def __init__(self, fast: int = 10, slow: int = 50):
        super().__init__()
        self.compute = False
        self.fast, self.slow = min(fast, slow), max(fast, slow)
        self.fast_col = f"SMA_{self.fast}"
        self.slow_col = f"SMA_{self.slow}"
        self.signal_col = f"signal_SMA_{self.fast}_{self.slow}"

    def generate_signal(self, df: pd.DataFrame) -> pd.DataFrame:
        # Compute if missing
        if self.signal_col in df.columns:
            return df
        if self.fast_col not in df.columns:
            df[self.fast_col] = ta.sma(df['close'], length=self.fast)
        if self.slow_col not in df.columns:
            df[self.slow_col] = ta.sma(df['close'], length=self.slow)

        # Signal logic: 1 = fast > slow (long), -1 = fast < slow (short)
        df[self.signal_col] = np.where(df[self.fast_col] > df[self.slow_col], 1, -1)
        self.compute = True
        return df
    
# =========================
# RSI Strategy
# =========================

class RSIStrategy(Strategy):
    def __init__(self, length=14, overbought=70, oversold=30):
        super().__init__()
        self.compute = False
        self.length = length
        self.overbought, self.oversold = max(overbought, oversold), min(overbought, oversold)
        self.indicator_col = f"RSI_{self.length}"
        self.signal_col = f"signal_RSI_{self.length}_{self.overbought}_{self.oversold}"

    def generate_signal(self, df: pd.DataFrame) -> pd.DataFrame:
        # Compute if missing
        if self.signal_col in df.columns:
            return df
        if self.indicator_col not in df.columns:
            df[self.indicator_col] = ta.rsi(df['close'], length=self.length)

        # Signal logic: 1 = oversold (long), -1 = overbought (short)
        rsi = df[self.indicator_col]
        df[self.signal_col] = np.where(rsi > self.overbought, -1,
                                np.where(rsi < self.oversold, 1, 0))
        self.compute = True
        return df

# =========================
# EMA Crossover Strategy
# =========================

class EMACrossoverStrategy(Strategy):
    def __init__(self, fast: int = 10, slow: int = 50):
        super().__init__()
        self.compute = False
        self.fast, self.slow = min(fast, slow), max(fast, slow)
        self.fast_col = f"EMA_{self.fast}"
        self.slow_col = f"EMA_{self.slow}"
        self.signal_col = f"signal_EMA_{self.fast}_{self.slow}"

    def generate_signal(self, df: pd.DataFrame) -> pd.DataFrame:
        # Compute if missing
        if self.signal_col in df.columns:
            return df
        if self.fast_col not in df.columns:
            df[self.fast_col] = ta.ema(df['close'], length=self.fast)
        if self.slow_col not in df.columns:
            df[self.slow_col] = ta.ema(df['close'], length=self.slow)

        # Signal logic: 1 = fast > slow (long), -1 = fast < slow (short)
        df[self.signal_col] = np.where(
            df[self.fast_col] > df[self.slow_col], 1, -1
        )
        self.compute = True
        return df

# =========================
# MACD Strategy
# =========================

class MACDStrategy(Strategy):
    def __init__(self, fast=12, slow=26, signal_length=9, include_hist=True):
        super().__init__()
        self.compute = False
        self.fast, self.slow = min(fast, slow), max(fast, slow)
        self.signal_length = signal_length
        self.include_hist = include_hist
        self.macd_col = f"MACD_{self.fast}_{self.slow}"
        self.signal_col = f"MACD_signal_{self.fast}_{self.slow}_{self.signal_length}"
        self.hist_col = f"MACD_hist_{self.fast}_{self.slow}_{self.signal_length}"
        self.signal_output_col = f"signal_MACD_{self.fast}_{self.slow}_{self.signal_length}"

    def generate_signal(self, df: pd.DataFrame):
        # Compute if missing
        if self.signal_output_col in df.columns:
            return df if self.include_hist else (df, df.get(self.hist_col, None))
        missing_cols = {
            'macd': self.macd_col not in df.columns,
            'signal': self.signal_col not in df.columns,
            'hist': self.include_hist and self.hist_col not in df.columns
        }

        if any(missing_cols.values()):
            macd = ta.macd(df['close'], fast=self.fast, slow=self.slow, signal=self.signal_length)

            if missing_cols['macd']:
                df[self.macd_col] = macd.iloc[:, 0]
            if missing_cols['signal']:
                df[self.signal_col] = macd.iloc[:, 1]
            if self.include_hist and missing_cols['hist']:
                df[self.hist_col] = macd.iloc[:, 2]

        # Signal logic: 1 = MACD > Signal (long), -1 = MACD < Signal (short)
        df[self.signal_output_col] = np.where(
            df[self.macd_col] > df[self.signal_col], 1, -1
        )
        self.compute = True
        return df if self.include_hist else (df, df[self.macd_col] - df[self.signal_col])


# =========================
# Bollinger Bands Strategy
# ========================= 


