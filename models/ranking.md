# Model ranking

Edit this file by hand after each run. Lower rank number is better. Rank by test model metrics, not by the backtest.

Best possible (metric ceilings): dir acc >60%, RMSE 0, MAE 0, MAPE 0%.

## Results


| Rank | Date       | Model            | Run                    | Features    | Feat scaler    | W   | H   | Dir acc | RMSE | MAE  | MAPE  |
| ---- | ---------- | ---------------- | ---------------------- | ----------- | -------------- | --- | --- | ------- | ---- | ---- | ----- |
| 1    | 2026-09-20 | lstm_logret      | logret_h2_stdscaler    | log_returns | StandardScaler | 200 | 2   | 50.5%   | 0.77 | 0.44 | 0.07% |
| 2    | 2026-09-19 | lstm_logret      | logret_h8_stdscaler    | log_returns | StandardScaler | 200 | 8   | 50.7%   | 1.09 | 0.69 | 0.09% |
| 3    | 2026-09-19 | lstm_baseline_v1 | raw_ohlcv_h8_stdscaler | raw_ohlcv   | StandardScaler | 200 | 8   | 49.7%   | 2.77 | 1.65 | 0.31% |


## Params and notes


| Rank | Run                    | Target scaler  | Min move | Dir  | TP    | SL    | Trades | Equity | Win rate | Notes                                                                                          |
| ---- | ---------------------- | -------------- | -------- | ---- | ----- | ----- | ------ | ------ | -------- | ---------------------------------------------------------------------------------------------- |
| 1    | logret_h2_stdscaler    | StandardScaler | 0%       | both | 0.50% | 0.50% | 3210   | 0.973  | 49.5%    | 2024-07 to 2026-05, embargo 202. Almost all timeouts (3180/3210). Dir acc still coin flip.     |
| 2    | logret_h8_stdscaler    | StandardScaler | 0.10%    | both | 0.30% | 0.30% | 0      | 1.000  | —        | 2025-08 to 2026-08, embargo 208. Preds ~0.003%; min move 0.10% so no trades.                    |
| 3    | raw_ohlcv_h8_stdscaler | StandardScaler | 0%       | both | 0.30% | 0.30% | 682    | 0.930  | 48.5%    | 2024-09 to 2025-04, leaky chrono split. Dir acc about coin flip.                               |
