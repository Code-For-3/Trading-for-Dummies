from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit

import vectorbt as vbt
import pandas as pd
import numpy as np
from datetime import datetime

from Alpaca_Credentials import ALPACA_API_KEY, ALPACA_SECRET_KEY
client = StockHistoricalDataClient(ALPACA_API_KEY, ALPACA_SECRET_KEY)

# Supported Timeframe
SUPPORTED_TIMEFRAMES = {
    "Minute": [1, 5, 15],
    "Hour": [1],
    "Day": [1]
}

# Fetch Alpaca Data - Standardized to match vectorbt.YFData output
def fetch_alpaca_vbt_data(symbol: str, start: str, end: str,
                           timeframe_unit: str = "Hour", multiplier: int = 1) -> pd.DataFrame:
    """
    Fetch OHLCV stock data from Alpaca and return in vectorbt-style DataFrame.
    Matches structure and types of vectorbt.YFData.get(["Open", "High", "Low", "Close", "Volume"]).
    """

    tf_unit_enum = TimeFrameUnit[timeframe_unit]
    timeframe = TimeFrame(multiplier, tf_unit_enum)

    request = StockBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=timeframe,
        start=datetime.strptime(start, "%Y-%m-%d"),
        end=datetime.strptime(end, "%Y-%m-%d")
    )

    bars = client.get_stock_bars(request).df

    # Flatten multi-index if needed
    if isinstance(bars.index, pd.MultiIndex):
        bars.index = bars.index.get_level_values("timestamp")

    # Handle multi-symbol case
    if isinstance(bars.columns, pd.MultiIndex):
        if symbol in bars.columns.levels[0]:
            bars = bars.xs(symbol, level=0, axis=1)
        else:
            raise KeyError(f"Symbol '{symbol}' not found in returned data.")

    # Standardize column names
    bars = bars.rename(columns={
        "open": "Open",
        "high": "High",
        "low": "Low",
        "close": "Close",
        "volume": "Volume"
    })

    # Ensure column order and types
    bars = bars[["Open", "High", "Low", "Close", "Volume"]]
    bars = bars.astype(np.float64)

    # Ensure proper datetime index
    bars.index = pd.to_datetime(bars.index)
    bars = bars.sort_index()
    bars.index.name = "timestamp"
    bars.columns.name = "field"

    return bars

def get_data_auto(symbol: str, start: str, end: str,
                  timeframe_unit: str = "Day", multiplier: int = 1) -> pd.DataFrame:
    """
    Automatically choose between Yahoo and Alpaca data based on timeframe.
    Formats all outputs to match vectorbt.YFData.get for consistency.
    """
    if timeframe_unit == "Day":
        yf_data = vbt.YFData.download(symbol, start=start, end=end)
        df = yf_data.get(["Open", "High", "Low", "Close", "Volume"])
    else:
        df = fetch_alpaca_vbt_data(symbol, start, end, timeframe_unit, multiplier)

    # Final format normalization
    df = df.astype(np.float64)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df.index.name = "timestamp"
    df.columns.name = "field"

    return df
