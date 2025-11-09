# Trading Strategy Framework

[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![API: Alpaca](https://img.shields.io/badge/API-Alpaca-black.svg)](https://alpaca.markets/)
[![Indicators: pandas--ta](https://img.shields.io/badge/Indicators-pandas--ta-yellow.svg)](https://github.com/twopirllc/pandas-ta)
[![Data: Yahoo Finance](https://img.shields.io/badge/Data-Yahoo%20Finance-purple.svg)](https://finance.yahoo.com/)
[![Visualization: Matplotlib](https://img.shields.io/badge/Visualization-Matplotlib-red.svg)](https://matplotlib.org/)

This repository provides a modular Python framework for fetching, analyzing, and visualizing stock data, as well as implementing and testing different trading strategies using **Alpaca API**, **pandas-ta**, and **matplotlib**.

---

## 📊 Features

- Fetch historical stock data from **Alpaca API**
- Automatic cleaning of non-trading days and missing data
- Built-in technical indicators using `pandas-ta`
- Customizable trading strategies:
  - Simple Moving Average (SMA) Crossover
  - Exponential Moving Average (EMA) Crossover
  - Relative Strength Index (RSI)
  - Moving Average Convergence Divergence (MACD)
- Candlestick and signal visualization
- Trade plotting with entry/exit markers

---

## ⚙️ Requirements

Install dependencies using:

```bash
pip install pandas numpy matplotlib pandas-ta yfinance alpaca-py scipy mplfinance
```

You will also need to set your Alpaca API credentials as environment variables:

```bash
export API_KEY="your_api_key"
export API_SECRET="your_api_secret"
```

---

## 🚀 Usage

### 1. Fetch Stock Data

```python
df = get_stock_data("AAPL", start_date="2023-01-01", end_date="2023-12-31")
```

### 2. Apply a Strategy

```python
from strategies import SMACrossoverStrategy

strategy = SMACrossoverStrategy(fast=10, slow=50)
df = strategy.generate_signal(df)
strategy.plot_trades(df)
```

### 3. Visualize Data

```python
plot_candlestick_with_volume(df, "AAPL")
plot_price_with_signals(df, indicators=["SMA_10", "SMA_50"])
```

---

## 🧠 Strategy Classes

Each strategy inherits from the base `Strategy` class and implements the `generate_signal()` method to produce buy/sell signals.

| Strategy | Description |
|-----------|--------------|
| **SMACrossoverStrategy** | Uses fast and slow moving averages to detect bullish or bearish trends |
| **EMACrossoverStrategy** | Similar to SMA but more responsive to recent data |
| **RSIStrategy** | Generates signals based on overbought/oversold RSI levels |
| **MACDStrategy** | Uses MACD and signal line crossovers |

---

## Example Screenshots

```bash
Date from: 2024-01-01
Date to: 2025-04-30

```

![Walk-Forward: Actual Return vs Optimized Value](images/walk_forward.png)
![Walk-Forward Equity](images/walk_forward_equity.png)


---

## 🧰 Future Improvements

- Add backtesting framework with performance metrics (Sharpe ratio, win rate, etc.)
- Support for cryptocurrency and forex pairs
- Integration with Plotly for interactive charts
- AI/ML-based signal generation

---

> _*Developed by Mario Portillo*_
