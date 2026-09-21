# Model ranking

Edit this file by hand after each run. Lower rank number is better. Rank by test model metrics, not by the backtest.

Best possible (metric ceilings): dir acc >60%, RMSE 0, MAE 0, MAPE 0%.

## Results


| Rank | Run                    | Features             | Feat scaler    | W   | H   | Dir acc | RMSE | MAE  | MAPE  |
| ---- | ---------------------- | -------------------- | -------------- | --- | --- | ------- | ---- | ---- | ----- |
| 1    | logret_h2_w78          | log_returns          | StandardScaler | 78  | 2   | 50.4%   | 0.77 | 0.44 | 0.06% |
| 2    | dir_bce_stacked_h2_w78 | log_returns_mid      | StandardScaler | 78  | 2   | 50.5%   | 0.77 | 0.44 | 0.06% |
| 3    | logret_h2_stdscaler    | log_returns          | StandardScaler | 200 | 2   | 50.5%   | 0.77 | 0.44 | 0.07% |
| 4    | logret_huber_h4_w78    | logret_mid_tod_range | StandardScaler | 78  | 4   | 50.9%   | 1.06 | 0.63 | 0.09% |
| 5    | logret_h8_stdscaler    | log_returns          | StandardScaler | 200 | 8   | 50.7%   | 1.09 | 0.69 | 0.09% |
| 6    | dir_bce_h6_w78_bigmove | logret_mid_tod_range | StandardScaler | 78  | 6   | 50.0%   | 1.29 | 0.79 | 0.12% |
| 7    | barrier_3cls_h6_w78         | logret_mid_tod_range     | StandardScaler | 78  | 6   | 25.1%   | 1.57 | 1.04 | 0.15% |
| 8    | barrier_gated_session_h6_w78 | logret_session_tod_range | StandardScaler | 78  | 6   | 48.4%   | 1.84 | 1.52 | 0.22% |
| 9    | barrier_hit_bce_h6_w78      | logret_mid_tod_range     | StandardScaler | 78  | 6   | 47.8%   | 1.89 | 1.54 | 0.23% |
| 10   | raw_ohlcv_h8_stdscaler      | raw_ohlcv                | StandardScaler | 200 | 8   | 49.7%   | 2.77 | 1.65 | 0.31% |




## Params and notes


| Rank | Run                    | Target scaler  | Min move | Dir  | TP    | SL    | Trades | Equity | Win rate | Notes                                                                                                                                                                                            |
| ---- | ---------------------- | -------------- | -------- | ---- | ----- | ----- | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | logret_h2_w78          | StandardScaler | 0%       | both | 0.20% | 0.20% | 3293   | 1.093  | 50.7%    | 2024-07 to 2026-05, embargo 80, epochs 50 / patience 8. Timeouts 2840; TP 222 / SL 207. Dir acc still ~50%.                                                                                      |
| 2    | dir_bce_stacked_h2_w78 | StandardScaler | 0%       | both | 0.20% | 0.20% | 3293   | 1.029  | 50.2%    | BCE P(up), LSTM 64/32 + dropout 0.2. Train/val dir 52.0%/51.8%, test 50.5%. Timeouts 2840; SL 219 / TP 210. Longs 2896 / shorts 397.                                                             |
| 3    | logret_h2_stdscaler    | StandardScaler | 0%       | both | 0.50% | 0.50% | 3210   | 0.973  | 49.5%    | 2024-07 to 2026-05, embargo 202. Almost all timeouts (3180/3210). Dir acc still coin flip.                                                                                                       |
| 4    | logret_huber_h4_w78    | StandardScaler | 0%       | both | 0.20% | 0.20% | 2150   | 0.930  | 50.7%    | Huber+sign BCE, LSTM 64/32, 9-d, recency. H=4 (not H=2). Train/val dir 51.4%/50.9%; test 50.9%. dir_acc_conf n=0 (preds <1bp). Timeouts 1455; TP 306 / SL 340. Longs 2147 / shorts 3.             |
| 5    | logret_h8_stdscaler    | StandardScaler | 0.10%    | both | 0.30% | 0.30% | 0      | 1.000  | —        | 2025-08 to 2026-08, embargo 208. Preds ~0.003%; min move 0.10% so no trades.                                                                                                                     |
| 6    | dir_bce_h6_w78_bigmove | StandardScaler | conf 8%  | both | 0.20% | 0.20% | 68     | 0.998  | 50.0%    | Train/val drop |ret|<0.10%. ES epoch 10 (best val epoch 2). Test dir_acc_big 50.0%; conf 51.7% (n=861). Timeouts 48; TP 10 / SL 10. Longs only (68). Null result.                                |
| 7    | barrier_3cls_h6_w78          | StandardScaler | P≥0.40   | both | 0.20% | 0.20% | 1134   | 1.006  | 50.2%    | Softmax timeout/up/down. Test cls_acc 58.7% (timeouts ~73%); side_acc 42.8%; side_acc_conf 29.3% (n=5721). Timeouts 434; TP 341 / SL 322. Longs 781 / shorts 353.                                |
| 8    | barrier_gated_session_h6_w78 | StandardScaler | conf 5%  | both | 0.20% | 0.20% | 281    | 0.965  | 44.5%    | Gated hits + session feats + recency. Train/val side 55.6%/55.3%; test 53.0%; conf 52.4% (n=361). ES epoch 18 (best val epoch 10). Timeouts 164; TP 55 / SL 58. Longs 47 / shorts 234.         |
| 9    | barrier_hit_bce_h6_w78       | StandardScaler | conf 5%  | both | 0.20% | 0.20% | 386    | 0.983  | 47.4%    | Hit-only BCE LSTM(32); skip range <0.30%. Train/val side 57.9%/58.5%; test side 50.2%; conf 53.3% (n=548). ES ~epoch 20 (best val epoch 12). Timeouts 251; TP 67 / SL 60. Longs 86 / shorts 300. |
| 10   | raw_ohlcv_h8_stdscaler       | StandardScaler | 0%       | both | 0.30% | 0.30% | 682    | 0.930  | 48.5%    | 2024-09 to 2025-04, leaky chrono split. Dir acc about coin flip.                                                                                                                                 |


