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
from scipy.stats import linregress


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

    df = df.reset_index()
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp')

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


# =========================
# RSI Indicator
# =========================

def calculate_rsi(df, period=14):
    # Make a copy of the dataframe to avoid modifying the original
    df_copy = df.copy()
    
    # Calculate daily price changes
    delta = df_copy['close'].diff()
    
    # Separate gains (up) and losses (down)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    
    # Calculate average gain and average loss over the specified period
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    
    # Calculate relative strength (RS)
    rs = avg_gain / avg_loss
    
    # Calculate RSI
    df_copy['rsi'] = 100 - (100 / (1 + rs))
    
    return df_copy


# =========================
# Signal Generation
# =========================

def generate_signals_rsi(df, overbought=70, oversold=30, period=14):
    result = df[['close']].copy()
    result['signal'] = 0
    
    # Calculate RSI
    rsi = calculate_rsi(df, period)['rsi']
    
    # Generate signals
    result.loc[rsi > overbought, 'signal'] = -1  # Sell signal when overbought
    result.loc[rsi < oversold, 'signal'] = 1  # Buy signal when oversold
    
    return result  # Returns DataFrame with 'close' and 'signal' columns

def generate_signals_mfi(df, overbought=80, oversold=20, period=14):
    result = df[['close']].copy() 
    result['signal'] = 0 
    
    # Calculate MFI
    mfi = calculate_mfi(df, period)['mfi']
    
    # Generate signals
    result.loc[mfi > overbought, 'signal'] = -1  # Sell signal when overbought
    result.loc[mfi < oversold, 'signal'] = 1  # Buy signal when oversold
    
    return result

def generate_combined_signal(df, rsi_period=14, mfi_period=14):
    result = df[['close']].copy()  # Keep close column
    result['signal'] = 0  # Initialize signals to 0
    
    # Calculate RSI and MFI
    rsi_df = calculate_rsi(df, rsi_period)
    mfi_df = calculate_mfi(df, mfi_period)
    
    # Generate signals
    # Strong buy signal (1) when both RSI < 30 and MFI < 20
    result.loc[(rsi_df['rsi'] < 30) & (mfi_df['mfi'] < 20), 'signal'] = 1
    
    # Strong sell signal (-1) when both RSI > 70 and MFI > 80
    result.loc[(rsi_df['rsi'] > 70) & (mfi_df['mfi'] > 80), 'signal'] = -1
    
    return result


# ===============================================
# Simple Moving Average Indicator
# ===============================================

def SimpleMA(df, small_window=20, long_window=50):
    result = df[['close']].copy()  # keep close column
    result['signal'] = 0

    sma = df['close'].rolling(window=small_window).mean()
    lma = df['close'].rolling(window=long_window).mean()

    result.loc[sma > lma, 'signal'] = 1
    result.loc[sma < lma, 'signal'] = -1

    return result



# ===============================================
# Backtesting Function
# ===============================================


def backtest(data, initial_cash=100, transaction_cost=0):
    """
    Backtests a long/short strategy with signal: 1 = long, -1 = short, 0 = close position.
    Uses full capital on each trade and compounds returns.
    """
    position = "flat"  # can be 'long', 'short', or 'flat'
    cash = initial_cash
    entry_price = 0
    trade_log = []
    equity_curve = []

    for i in range(1, len(data)):
        signal = data['signal'].iloc[i]
        price = data['close'].iloc[i]
        timestamp = data.index[i]

        # Track equity at each step
        equity_curve.append((timestamp, cash))

        # === CLOSE LOGIC ===
        if signal == 0 and position != "flat":
            if position == "long":
                pnl = (price - entry_price - transaction_cost) / entry_price
            elif position == "short":
                pnl = (entry_price - price - transaction_cost) / entry_price
            cash *= (1 + pnl)
            trade_log.append({
                'timestamp': timestamp,
                'action': 'close',
                'position': position,
                'price': price,
                'pnl': pnl,
                'cash': cash
            })
            position = "flat"

        # === FLIP LOGIC ===
        elif signal == 1 and position == "short":
            pnl = (entry_price - price - transaction_cost) / entry_price
            cash *= (1 + pnl)
            trade_log.append({
                'timestamp': timestamp,
                'action': 'flip_to_long',
                'price': price,
                'pnl': pnl,
                'cash': cash
            })
            entry_price = price
            position = "long"

        elif signal == -1 and position == "long":
            pnl = (price - entry_price - transaction_cost) / entry_price
            cash *= (1 + pnl)
            trade_log.append({
                'timestamp': timestamp,
                'action': 'flip_to_short',
                'price': price,
                'pnl': pnl,
                'cash': cash
            })
            entry_price = price
            position = "short"

        # === ENTER NEW POSITION ===
        elif signal == 1 and position == "flat":
            entry_price = price
            position = "long"
            trade_log.append({
                'timestamp': timestamp,
                'action': 'buy',
                'price': price
            })

        elif signal == -1 and position == "flat":
            entry_price = price
            position = "short"
            trade_log.append({
                'timestamp': timestamp,
                'action': 'sell_short',
                'price': price
            })

    # Final equity entry
    if len(data) > 0:
        equity_curve.append((data.index[-1], cash))

    # Convert to equity Series
    index = [ts[1] if isinstance(ts, tuple) else ts for (ts, _) in equity_curve]
    equity_series = pd.Series(
        data=[val for (_, val) in equity_curve],
        index=pd.to_datetime(index)
    )

    return equity_series, trade_log


def backtest_signals(data, initial_cash=1000, risk_per_trade=0.01, leverage=1):
    in_position = False
    position_type = None  # 'long' or 'short'
    entry_price = 0
    position_size = 0
    cash = initial_cash
    trade_log = []
    equity_curve = []

    for i in range(1, len(data)):
        signal = data['signal'].iloc[i]
        price = data['close'].iloc[i]
        timestamp = data.index[i]

        equity_curve.append((timestamp, cash))

        # === ENTER LONG/SHORT ===
        if not in_position and signal in [1, -1]:
            entry_price = price
            risk_amount = cash * risk_per_trade * leverage
            position_size = risk_amount / price
            position_type = 'long' if signal == 1 else 'short'
            in_position = True

            trade_log.append({
                'timestamp': timestamp,
                'action': 'entry',
                'side': position_type,
                'entry_price': entry_price,
                'size': position_size
            })

        # === EXIT ON 0 SIGNAL OR FLIP ===
        elif in_position:
            should_exit = (
                (signal == 0) or
                (position_type == 'long' and signal == -1) or
                (position_type == 'short' and signal == 1)
            )

            if should_exit:
                exit_price = price
                pnl = (
                    (exit_price - entry_price) * position_size
                    if position_type == 'long'
                    else (entry_price - exit_price) * position_size
                )
                cash += pnl
                in_position = False

                trade_log.append({
                    'timestamp': timestamp,
                    'action': 'exit',
                    'side': position_type,
                    'exit_price': exit_price,
                    'pnl': pnl,
                    'cash': cash
                })

                # === If flipping direction, immediately re-enter ===
                if signal in [1, -1]:
                    entry_price = price
                    risk_amount = cash * risk_per_trade * leverage
                    position_size = risk_amount / price
                    position_type = 'long' if signal == 1 else 'short'
                    in_position = True

                    trade_log.append({
                        'timestamp': timestamp,
                        'action': 'entry',
                        'side': position_type,
                        'entry_price': entry_price,
                        'size': position_size
                    })

    # Final equity snapshot
    if len(data) > 0:
        equity_curve.append((data.index[-1], cash))

    equity_series = pd.Series(
        data=[val for (_, val) in equity_curve],
        index=pd.to_datetime([ts for (ts, _) in equity_curve])
    )

    return equity_series, trade_log



# ===============================================
# Evaluate Performance
# ===============================================

def evaluate_performance(equity_series, trade_log, initial_cash=10_000, benchmark_symbol="SPY"):
    """
    Evaluates strategy performance metrics based on equity curve and trade log.
    """
    equity_series = equity_series.sort_index().astype(float)

    if equity_series.empty or not trade_log:
        return {"error": "Insufficient data to evaluate performance."}

    final_cash = equity_series.iloc[-1]
    total_return = (final_cash - initial_cash) / initial_cash

    # Determine frequency for annualization
    index_deltas = equity_series.index.to_series().diff().dropna()
    median_delta = index_deltas.median()
    periods_per_year = {
        pd.Timedelta("1min"): 252 * 390,
        pd.Timedelta("5min"): 252 * 78,
        pd.Timedelta("15min"): 252 * 26,
        pd.Timedelta("1H"): 252 * 6.5,
        pd.Timedelta("1D"): 252
    }
    closest_freq = min(periods_per_year.keys(), key=lambda x: abs(x - median_delta))
    freq = periods_per_year[closest_freq]

    # Strategy returns
    returns = equity_series.pct_change().dropna()
    annualized_return = (1 + total_return) ** (freq / len(returns)) - 1 if not returns.empty else 0
    volatility = returns.std() * np.sqrt(freq)
    sharpe = (returns.mean() / returns.std()) * np.sqrt(freq) if returns.std() != 0 else 0

    # Sortino ratio
    downside = returns[returns < 0]
    sortino = (returns.mean() / downside.std()) * np.sqrt(freq) if not downside.empty else 0

    # Max drawdown
    rolling_max = equity_series.cummax()
    drawdown = (equity_series - rolling_max) / rolling_max
    max_drawdown = drawdown.min()

    # Exposure
    in_market_steps = sum(1 for t in trade_log if t['action'] == 'buy')
    exposure = in_market_steps / len(equity_series)

    # --- ALPHA/BETA using return alignment (robust) ---
    # Get SPY data
    spy_df = get_stock_data(
        benchmark_symbol,
        equity_series.index[0].strftime("%Y-%m-%d"),
        equity_series.index[-1].strftime("%Y-%m-%d"),
        timeframe_unit="Day", multiplier=1
    )

    # Compute returns
    strategy_returns = equity_series.pct_change().dropna()
    spy_returns = spy_df['close'].pct_change().dropna()

    # Drop duplicate timestamps
    strategy_returns = strategy_returns[~strategy_returns.index.duplicated()]
    spy_returns = spy_returns[~spy_returns.index.duplicated()]

    # Join on common timestamps
    returns_df = pd.concat([strategy_returns, spy_returns], axis=1, join='inner')
    returns_df.columns = ['strategy', 'spy']
    returns_df.dropna(inplace=True)

    # Compute beta and alpha
    if not returns_df.empty:
        slope, intercept, r_value, p_value, std_err = linregress(
            returns_df['spy'], returns_df['strategy']
        )
        beta = slope
        alpha = (returns_df['strategy'].mean() - beta * returns_df['spy'].mean()) * freq
    else:
        beta = np.nan
        alpha = np.nan


    # Final result
    return {
        "Final Cash": round(final_cash, 2),
        "Total Return (%)": round(total_return * 100, 2),
        "Annualized Return (%)": round(annualized_return * 100, 2),
        "Sharpe Ratio": round(sharpe, 2),
        "Sortino Ratio": round(sortino, 2),
        "Volatility (%)": round(volatility * 100, 2),
        "Max Drawdown (%)": round(max_drawdown * 100, 2),
        "Alpha vs SPY (%)": round(alpha * 100, 2) if not np.isnan(alpha) else None,
        "Beta vs SPY": round(beta, 2) if not np.isnan(beta) else None,
        "Exposure (%)": round(exposure * 100, 2),
        "Frequency Used": str(closest_freq)
    }


# ===============================================
# Evaluate Trades
# ===============================================

def evaluate_trades(trade_log):
    """
    Evaluate detailed statistics for individual trades.
    Assumes alternating buy/sell pairs and PnL only on sell actions.
    """
    if not trade_log:
        return {"error": "Trade log is empty."}

    trades = []
    current_trade = {}

    for trade in trade_log:
        # Extract plain timestamp even if it's a tuple
        ts = trade['timestamp'][1] if isinstance(trade['timestamp'], tuple) else trade['timestamp']

        if trade['action'] == 'buy':
            current_trade = {'entry_time': ts, 'entry_price': trade['price']}
        elif trade['action'] == 'sell' and current_trade:
            exit_time = ts
            exit_price = trade['price']
            pnl = trade['pnl']

            duration = (exit_time - current_trade['entry_time']).total_seconds() / 60  # minutes
            trades.append({
                'pnl': pnl,
                'duration_min': duration,
                'entry_time': current_trade['entry_time'],
                'exit_time': exit_time
            })
            current_trade = {}

    if not trades:
        return {"error": "No completed buy/sell pairs found."}

    df = pd.DataFrame(trades)

    wins = df[df['pnl'] > 0]
    losses = df[df['pnl'] < 0]

    win_rate = len(wins) / len(df)
    avg_pnl = df['pnl'].mean()
    expectancy = (win_rate * wins['pnl'].mean()) - ((1 - win_rate) * abs(losses['pnl'].mean())) if not losses.empty else wins['pnl'].mean()

    return {
        "Number of Trades": len(df),
        "Win Rate (%)": round(win_rate * 100, 2),
        "Avg PnL": round(avg_pnl, 2),
        "Best Trade": round(df['pnl'].max(), 2),
        "Worst Trade": round(df['pnl'].min(), 2),
        "Avg Win": round(wins['pnl'].mean(), 2) if not wins.empty else None,
        "Avg Loss": round(losses['pnl'].mean(), 2) if not losses.empty else None,
        "Reward:Risk Ratio": round(wins['pnl'].mean() / abs(losses['pnl'].mean()), 2)
                             if not wins.empty and not losses.empty else None,
        "Avg Duration (min)": round(df['duration_min'].mean(), 2),
        "Win Std Dev": round(wins['pnl'].std(), 2) if len(wins) > 1 else 0,
        "Loss Std Dev": round(losses['pnl'].std(), 2) if len(losses) > 1 else 0,
        "Expectancy": round(expectancy, 2)
    }