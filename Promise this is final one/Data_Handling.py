from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame, TimeFrameUnit

import numpy as np
import pandas as pd
from numba import njit
from datetime import datetime
import talib
import vectorbt as vbt
from vectorbt.indicators.factory import IndicatorFactory

import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter
from itertools import product
import optuna
from sklearn.linear_model import LinearRegression
from scipy.stats import linregress, pearsonr


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



































def crop_with_padding_with_params(grid: np.ndarray, param_levels: dict, pad: int = 3):
    nonzero_mask = grid != 0
    coords = np.argwhere(nonzero_mask)

    if coords.size == 0:
        raise ValueError("Grid contains only zeros")

    min_bounds = coords.min(axis=0)
    max_bounds = coords.max(axis=0) + 1  # inclusive

    slices = []
    cropped_param_levels = {}

    for i, (param_name, values) in enumerate(param_levels.items()):
        start = max(min_bounds[i] - pad, 0)
        end = min(max_bounds[i] + pad, len(values))

        slices.append(slice(start, end))
        cropped_param_levels[param_name] = values[start:end]

    cropped_grid = grid[tuple(slices)]
    return cropped_grid, slices, cropped_param_levels




def Overfitting_reduction(pf, objective_function=None, smoothing_size=3, filter_threshold=0.0):
    # Step 1: Compute raw result grid
    if objective_function is not None:
        results = objective_function(pf)
    else:
        results = pf.total_return().values

    # Step 2: Extract parameter structure
    multi_index = pf.wrapper.columns
    param_df = pd.DataFrame(multi_index.tolist(), columns=multi_index.names)
    param_levels = {col: np.unique(param_df[col]) for col in param_df.columns}
    shape = tuple(len(param_levels[col]) for col in param_df.columns)

    # Step 3: Reshape results
    reshaped = results.reshape(shape)

    # Step 4: Smooth
    smoothed_grid = uniform_filter(reshaped, size=smoothing_size)

    # Step 5: Filter
    filtered_grid = np.where(smoothed_grid > filter_threshold, smoothed_grid, 0.0)

    # Step 6: Crop grid and adjust parameter levels
    final_grid, slices, cropped_param_levels = crop_with_padding_with_params(filtered_grid, param_levels, pad=smoothing_size)

    # Step 7: Build MultiIndex Series from N-D grid
    param_names = list(cropped_param_levels.keys())
    param_values = list(cropped_param_levels.values())
    combos = list(product(*param_values))  # Cartesian product
    score_series = pd.Series(final_grid.flatten(), index=pd.MultiIndex.from_tuples(combos, names=param_names))

    # Step 8: Get best parameters and portfolio
    best_param_tuple = score_series.idxmax()
    best_value = score_series.loc[best_param_tuple]
    best_portfolio = pf[best_param_tuple]
    best_params = dict(zip(param_names, best_param_tuple))

    return best_params, best_value, best_portfolio


def Overfitting_reduction_simpler(pf, objective_function=None, smoothing_size=3, filter_threshold=0.0):
    # Step 1: Compute raw result grid
    if objective_function is not None:
        results = objective_function(pf)
    else:
        results = pf.total_return().values

    # Step 2: Extract parameter structure
    multi_index = pf.wrapper.columns
    param_df = pd.DataFrame(multi_index.tolist(), columns=multi_index.names)
    param_levels = {col: np.unique(param_df[col]) for col in param_df.columns}
    shape = tuple(len(param_levels[col]) for col in param_df.columns)

    # Step 3: Reshape results
    reshaped = results.reshape(shape)

    # Step 4: Smooth
    smoothed_grid = uniform_filter(reshaped, size=smoothing_size)

    # Step 5: Filter
    filtered_grid = np.where(smoothed_grid > filter_threshold, smoothed_grid, 0.0)

    # Step 6: Skip cropping - use full filtered grid
    param_names = list(param_levels.keys())
    param_values = list(param_levels.values())
    combos = list(product(*param_values))  # Cartesian product
    score_series = pd.Series(filtered_grid.flatten(), index=pd.MultiIndex.from_tuples(combos, names=param_names))

    # Step 7: Get best parameters and portfolio
    best_param_tuple = score_series.idxmax()
    best_value = score_series.loc[best_param_tuple]
    best_portfolio = pf[best_param_tuple]
    best_params = dict(zip(param_names, best_param_tuple))

    return best_params, best_value, best_portfolio


def Overfitting_reduction_simplest(pf, objective_function=None, smoothing_size=3):
    # Step 1: Compute raw result grid
    if objective_function is not None:
        results = objective_function(pf)
    else:
        results = pf.total_return().values

    # Step 2: Extract parameter structure
    multi_index = pf.wrapper.columns
    param_df = pd.DataFrame(multi_index.tolist(), columns=multi_index.names)
    param_levels = {col: np.unique(param_df[col]) for col in param_df.columns}
    shape = tuple(len(param_levels[col]) for col in param_df.columns)

    # Step 3: Reshape results
    reshaped = results.reshape(shape)

    # Step 4: Smooth
    smoothed_grid = uniform_filter(reshaped, size=smoothing_size)

    # Step 6: Skip cropping - use full filtered grid
    param_names = list(param_levels.keys())
    param_values = list(param_levels.values())
    combos = list(product(*param_values))  # Cartesian product
    score_series = pd.Series(smoothed_grid.flatten(), index=pd.MultiIndex.from_tuples(combos, names=param_names))

    # Step 7: Get best parameters and portfolio
    best_param_tuple = score_series.idxmax()
    best_value = score_series.loc[best_param_tuple]
    best_portfolio = pf[best_param_tuple]
    best_params = dict(zip(param_names, best_param_tuple))

    return best_params, best_value, best_portfolio




def build_signals_from_trade_indices(trades_df, full_index):
    entries = pd.Series(False, index=full_index)
    exits = pd.Series(False, index=full_index)

    for _, row in trades_df.iterrows():
        entry_idx = int(row['entry_idx'])
        exit_idx = int(row['exit_idx'])

        if 0 <= entry_idx < len(full_index):
            entries.iloc[entry_idx] = True
        if 0 <= exit_idx < len(full_index):
            exits.iloc[exit_idx] = True

    return entries, exits






def plot_trade_frequency_distribution_per_day(all_trades, data):
    all_trades_df = pd.concat(all_trades, ignore_index=True)

    # Map entry indices to timestamps and normalize to dates
    all_trades_df['entry_time'] = data.index[all_trades_df['entry_idx']]
    all_trades_df['entry_date'] = all_trades_df['entry_time'].dt.normalize()

    # Count trades per day
    daily_trade_counts = all_trades_df['entry_date'].value_counts()

    # Count how often each number of trades per day occurs
    trade_count_distribution = daily_trade_counts.value_counts().sort_index()

    plt.figure(figsize=(12, 6))
    trade_count_distribution.plot(kind='bar')
    plt.title('Distribution of Number of Trades per Day')
    plt.xlabel('Trades in a Day')
    plt.ylabel('Number of Days')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_trade_return_distribution_from_pf(portfolio):
    trade_returns = portfolio.trades.records['return'] * 100 
    
    plt.figure(figsize=(12, 6))
    plt.hist(trade_returns, bins=40, edgecolor='black')
    plt.title("Distribution of All Trade Returns (%)")
    plt.xlabel("Trade Return (%)")
    plt.ylabel("Number of Trades")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_portfolios_return_distribution(all_pf, bins=30):
    # Extract and convert returns to %
    daily_returns = [entry["Portfolios"].total_return() * 100 for entry in all_pf]
    daily_returns_pdS = pd.Series(daily_returns)

    plt.figure(figsize=(12, 6))
    daily_returns_pdS.plot(kind='hist', bins=bins, edgecolor='black', color='mediumseagreen')
    plt.title("Distribution of each Portfolio period Returns (%)")
    plt.xlabel("Total Return (%)")
    plt.ylabel("Number of Portfolios")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_expected_vs_actual_returns(all_pf):
    # Extract expected and actual returns
    expected_returns = [entry["Expected Returns"] for entry in all_pf]
    actual_returns = [entry["Portfolios"].total_return() for entry in all_pf]

    X = np.array(expected_returns).reshape(-1, 1)
    y = np.array(actual_returns)

    # Fit linear model
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # Regression stats
    slope, intercept, r_value, p_value, std_err = linregress(expected_returns, actual_returns)
    corr_coef, _ = pearsonr(expected_returns, actual_returns)

    # Plot
    plt.figure(figsize=(12, 6))
    plt.scatter(expected_returns, actual_returns, alpha=0.7, label='Actual vs Expected')
    plt.plot(expected_returns, y_pred, color='red', label='Fit Line')
    plt.title("Expected vs Actual Returns (Walk-Forward)")
    plt.xlabel("Expected Return")
    plt.ylabel("Actual Return")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Show stats on plot
    plt.figtext(
        0.15, 0.01,
        f"R² = {r_value**2:.3f}, p = {p_value:.3e}, r = {corr_coef:.3f}, Slope = {slope:.3f}, Intercept = {intercept:.3f}",
        fontsize=10
    )

    plt.show()


def plot_trades_per_portfolio(all_trades, all_pf):
    # Count trades in each test window
    num_trades = [len(trades_df) for trades_df in all_trades]
    returns = [entry["Portfolios"].total_return() for entry in all_pf]
    returns = [entry["Portfolios"].total_return() for entry in all_pf]
    colors = ['green' if ret > 0 else 'red' for ret in returns]
    # Create labels like pf0, pf1, ...
    pf_labels = [f"pf{i}" for i in range(len(all_trades))]
    x = list(range(len(all_trades)))

    # Plot
    plt.figure(figsize=(12, 6))
    plt.bar(x, num_trades, color=colors, edgecolor='black')
    plt.title("Number of Trades per Walk-Forward Portfolio")
    plt.xlabel("Portfolio")
    plt.ylabel("Number of Trades")
    plt.xticks(rotation=45)
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()