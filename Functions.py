# Install Libraries
#!pip install alpaca-py
#!pip install mplfinance

# Import Libraries
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit
from datetime import datetime
import pandas as pd
import numpy as np


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


# =========================
# MFI Indicator
# =========================

def calculate_mfi(df, period=14):
    # Make a copy of the dataframe to avoid modifying the original
    df_copy = df.copy()
    
    # Calculate typical price
    df_copy['typical_price'] = (df_copy['high'] + df_copy['low'] + df_copy['close']) / 3
    
    # Calculate raw money flow
    df_copy['money_flow'] = df_copy['typical_price'] * df_copy['volume']
    
    # Get price direction: 1 if price went up, -1 if price went down
    df_copy['price_direction'] = np.where(
        df_copy['typical_price'] > df_copy['typical_price'].shift(1), 1, -1)
    
    # Separate positive and negative money flow
    df_copy['positive_money_flow'] = np.where(
        df_copy['price_direction'] > 0, df_copy['money_flow'], 0)
    df_copy['negative_money_flow'] = np.where(
        df_copy['price_direction'] < 0, df_copy['money_flow'], 0)
    
    # Calculate positive and negative money flow sums for the period
    df_copy['positive_money_flow_sum'] = df_copy['positive_money_flow'].rolling(window=period).sum()
    df_copy['negative_money_flow_sum'] = df_copy['negative_money_flow'].rolling(window=period).sum()
    
    # Calculate money flow ratio
    df_copy['money_flow_ratio'] = df_copy['positive_money_flow_sum'] / df_copy['negative_money_flow_sum']
    
    # Calculate MFI
    df_copy['mfi'] = 100 - (100 / (1 + df_copy['money_flow_ratio']))
    
    # Return original dataframe with MFI
    return df_copy[['open', 'high', 'low', 'close', 'volume', 'mfi']]
