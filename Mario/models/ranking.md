# Model ranking

Edit this file by hand after each run. Lower rank number is better. Rank by test model metrics, not by the backtest.

Best possible (metric ceilings): dir acc >60%, RMSE 0, MAE 0, MAPE 0%.

## Results

Each table is one model. Rank is inside that table only (lower RMSE, then MAE, then MAPE).

### Log-return MSE (`lstm_logret`)

Same net and label. Runs differ by window and horizon.

| Rank | Run                 | Features    | Feat scaler    | W   | H   | Dir acc | RMSE | MAE  | MAPE  |
| ---- | ------------------- | ----------- | -------------- | --- | --- | ------- | ---- | ---- | ----- |
| 1    | logret_h2_w78       | log_returns | StandardScaler | 78  | 2   | 50.4%   | 0.77 | 0.44 | 0.06% |
| 2    | logret_h2_stdscaler | log_returns | StandardScaler | 200 | 2   | 50.5%   | 0.77 | 0.44 | 0.07% |
| 3    | logret_h8_stdscaler | log_returns | StandardScaler | 200 | 8   | 50.7%   | 1.09 | 0.69 | 0.09% |

### Direction BCE

Predict P(up). Runs differ by horizon, features, and confidence filter.

| Rank | Run                    | Features             | Feat scaler    | W   | H   | Dir acc | RMSE | MAE  | MAPE  |
| ---- | ---------------------- | -------------------- | -------------- | --- | --- | ------- | ---- | ---- | ----- |
| 1    | dir_bce_stacked_h2_w78 | log_returns_mid      | StandardScaler | 78  | 2   | 50.5%   | 0.77 | 0.44 | 0.06% |
| 2    | dir_bce_h6_w78_bigmove | logret_mid_tod_range | StandardScaler | 78  | 6   | 50.0%   | 1.29 | 0.79 | 0.12% |

### Huber + sign BCE

LSTM 64/32, Huber plus a small sign loss, recency weights. Runs differ by features and horizon.

| Rank | Run                         | Features             | Feat scaler    | W   | H   | Dir acc | RMSE | MAE  | MAPE  |
| ---- | --------------------------- | -------------------- | -------------- | --- | --- | ------- | ---- | ---- | ----- |
| 1    | logret_ocv_mid_range_h2_w78 | logret_ocv_mid_range | StandardScaler | 78  | 2   | 50.1%   | 0.77 | 0.44 | 0.06% |
| 2    | logret_huber_h4_w78         | logret_mid_tod_range | StandardScaler | 78  | 4   | 50.9%   | 1.06 | 0.63 | 0.09% |

### Vol-scaled return

Target is a vol-scaled return, decoded back to dollars.

| Rank | Run                 | Features             | Feat scaler    | W   | H   | Dir acc | RMSE | MAE  | MAPE  |
| ---- | ------------------- | -------------------- | -------------- | --- | --- | ------- | ---- | ---- | ----- |
| 1    | volz_persist_h2_w78 | logret_ocv_mid_range | StandardScaler | 78  | 2   | 50.0%   | 0.77 | 0.44 | 0.06% |

### Barrier (TP / SL / timeout)

Same horizon and window. Runs differ by label (3-class, gated hit, hit-only BCE) and features.

| Rank | Run                          | Features                 | Feat scaler    | W   | H   | Dir acc | RMSE | MAE  | MAPE  |
| ---- | ---------------------------- | ------------------------ | -------------- | --- | --- | ------- | ---- | ---- | ----- |
| 1    | barrier_3cls_h6_w78          | logret_mid_tod_range     | StandardScaler | 78  | 6   | 25.1%   | 1.57 | 1.04 | 0.15% |
| 2    | barrier_gated_session_h6_w78 | logret_session_tod_range | StandardScaler | 78  | 6   | 48.4%   | 1.84 | 1.52 | 0.22% |
| 3    | barrier_hit_bce_h6_w78       | logret_mid_tod_range     | StandardScaler | 78  | 6   | 47.8%   | 1.89 | 1.54 | 0.23% |

### Raw OHLCV baseline (`lstm_baseline_v1`)

| Rank | Run                    | Features  | Feat scaler    | W   | H   | Dir acc | RMSE | MAE  | MAPE  |
| ---- | ---------------------- | --------- | -------------- | --- | --- | ------- | ---- | ---- | ----- |
| 1    | raw_ohlcv_h8_stdscaler | raw_ohlcv | StandardScaler | 200 | 8   | 49.7%   | 2.77 | 1.65 | 0.31% |

### London / NYC session (dominant move)

Two samples per day at session open. London 08:00–14:30 `Europe/London`, NYC 09:30–16:00 `America/New_York`. Target is the larger move from the open (high vs low). Rank inside this table by **test dir acc** (called the bigger wick). `RMSE_y` is only filled for the signed-MSE runs.

`dir_touch` uses that run's own level. The 2022 row counts a touch when the session extreme reaches 0.20% from the open (past 0.40% still counts). The mag row counts a touch when the extreme reaches 80% of the predicted wick. Earlier rows use their own `|pred|`.

| Rank | Run                           | Features           | Feat scaler    | W   | Dir acc | RMSE_y | MAE_y  | dir_touch | skill vs 0 |
| ---- | ----------------------------- | ------------------ | -------------- | --- | ------- | ------ | ------ | --------- | ---------- |
| 1    | session_side_bce_l16_2022     | logret_gap_prevdom | StandardScaler | 156 | 55.6%   | —      | —      | 68.0%     | —          |
| 2    | session_side_bce_l16_2022_mag | logret_gap_prevdom | StandardScaler | 156 | 55.6%   | —      | 0.0041 | 19.9%     | —          |
| 3    | session_side_bce_l16          | logret_gap_prevdom | StandardScaler | 156 | 54.5%   | —      | —      | 34.3%     | —          |
| 4    | session_dom_signed_mse        | log_returns        | StandardScaler | 78  | 49.3%   | 0.0092 | 0.0077 | 94.0%     | 1.004      |
| 5    | session_side_bce_gap          | logret_gap_prevdom | StandardScaler | 156 | 49.3%   | —      | —      | 32.8%     | —          |
| 6    | session_side_plus_mag         | log_returns        | StandardScaler | 78  | 46.3%   | 0.0141 | 0.0109 | 14.9%     | 1.549      |




## Params and notes


| Rank | Run                          | Target scaler  | Min move | Dir  | TP    | SL    | Trades | Equity | Win rate | Notes                                                                                                                                                                                            |
| ---- | ---------------------------- | -------------- | -------- | ---- | ----- | ----- | ------ | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | logret_h2_w78                | StandardScaler | 0%       | both | 0.20% | 0.20% | 3293   | 1.093  | 50.7%    | 2024-07 to 2026-05, embargo 80, epochs 50 / patience 8. Timeouts 2840; TP 222 / SL 207. Dir acc still ~50%.                                                                                      |
| 2    | dir_bce_stacked_h2_w78       | StandardScaler | 0%       | both | 0.20% | 0.20% | 3293   | 1.029  | 50.2%    | BCE P(up), LSTM 64/32 + dropout 0.2. Train/val dir 52.0%/51.8%, test 50.5%. Timeouts 2840; SL 219 / TP 210. Longs 2896 / shorts 397.                                                             |
| 3    | logret_h2_stdscaler          | StandardScaler | 0%       | both | 0.50% | 0.50% | 3210   | 0.973  | 49.5%    | 2024-07 to 2026-05, embargo 202. Almost all timeouts (3180/3210). Dir acc still coin flip.                                                                                                       |
| 4    | logret_ocv_mid_range_h2_w78  | StandardScaler | 0%       | both | —     | —     | 3240   | 0.969  | 48.0%    | 5-d OCV+mid+range; close-at-H (no TP/SL). Huber+sign BCE, LSTM 64/32, recency. Train/val/test dir 51.2%/50.9%/50.1%. RMSE 0.769. horizon_close 3235 / flatten 5. Longs 2926 / shorts 314.       |
| 5    | volz_persist_h2_w78          | StandardScaler | 0%       | both | —     | —     | 3240   | 0.969  | 48.3%    | Vol-scaled y_z; decode to dollars. Persist RMSE 0.7692; LSTM 0.7691; skill 0.9998 (no beat). Train/val/test dir 51.1%/51.2%/50.0%; dir_acc_vol 50.3% (n=2855). horizon_close 3237 / flatten 3. Longs 2946 / shorts 294. |
| 6    | logret_huber_h4_w78          | StandardScaler | 0%       | both | 0.20% | 0.20% | 2150   | 0.930  | 50.7%    | Huber+sign BCE, LSTM 64/32, 9-d, recency. H=4 (not H=2). Train/val dir 51.4%/50.9%; test 50.9%. dir_acc_conf n=0 (preds <1bp). Timeouts 1455; TP 306 / SL 340. Longs 2147 / shorts 3.            |
| 7    | logret_h8_stdscaler          | StandardScaler | 0.10%    | both | 0.30% | 0.30% | 0      | 1.000  | —        | 2025-08 to 2026-08, embargo 208. Preds ~0.003%; min move 0.10% so no trades.                                                                                                                     |
| 8    | dir_bce_h6_w78_bigmove       | StandardScaler | conf 8%  | both | 0.20% | 0.20% | 68     | 0.998  | 50.0%    | Train/val drop                                                                                                                                                                                   |
| 9    | barrier_3cls_h6_w78          | StandardScaler | P≥0.40   | both | 0.20% | 0.20% | 1134   | 1.006  | 50.2%    | Softmax timeout/up/down. Test cls_acc 58.7% (timeouts ~73%); side_acc 42.8%; side_acc_conf 29.3% (n=5721). Timeouts 434; TP 341 / SL 322. Longs 781 / shorts 353.                                |
| 10   | barrier_gated_session_h6_w78 | StandardScaler | conf 5%  | both | 0.20% | 0.20% | 281    | 0.965  | 44.5%    | Gated hits + session feats + recency. Train/val side 55.6%/55.3%; test 53.0%; conf 52.4% (n=361). ES epoch 18 (best val epoch 10). Timeouts 164; TP 55 / SL 58. Longs 47 / shorts 234.           |
| 11   | barrier_hit_bce_h6_w78       | StandardScaler | conf 5%  | both | 0.20% | 0.20% | 386    | 0.983  | 47.4%    | Hit-only BCE LSTM(32); skip range <0.30%. Train/val side 57.9%/58.5%; test side 50.2%; conf 53.3% (n=548). ES ~epoch 20 (best val epoch 12). Timeouts 251; TP 67 / SL 60. Longs 86 / shorts 300. |
| 12   | raw_ohlcv_h8_stdscaler       | StandardScaler | 0%       | both | 0.30% | 0.30% | 682    | 0.930  | 48.5%    | 2024-09 to 2025-04, leaky chrono split. Dir acc about coin flip.                                                                                                                                 |
| 13   | session_dom_signed_mse       | StandardScaler | 0%       | both | —     | —     | 134    | 0.987  | 47.0%    | London 08:00–14:30 / NYC 09:30–16:00. LSTM(32) MSE on signed dominant y. Preds ~3.6 bp so touch 94% is easy. Always-long 51.5%. London/NYC dir 46.3%/52.2%. RMSE_y 0.0092 skill 1.004. Extreme $ RMSE 6.14. Longs 27 / shorts 107. Exit session close. |
| 14   | session_side_plus_mag        | StandardScaler | 0%       | both | —     | —     | 134    | 0.899  | 45.5%    | Two heads: BCE side + MSE mag. mean \|pred\| 0.86% vs mean \|y\| 0.76%. Test dir 46.3% vs always-long 51.5%. London/NYC 50.7%/41.8%. RMSE_y 0.0141 skill 1.549. Extreme $ RMSE 9.54. Longs 75 / shorts 59. Exit session close. |
| 15   | session_side_bce_gap         | —              | 0%       | both | —     | —     | 134    | 0.932  | 48.5%    | Side-only BCE + gap/prev_dom/is_nyc/range, W=156, LSTM(32), early-stop val_accuracy. Train/val/test dir 56.5%/56.0%/49.3%. Test lost to always-long 51.5%. London/NYC 52.2%/46.3%. touch 32.8%. Longs 75 / shorts 59. |
| 16   | session_side_bce_l16         | —              | 0%       | both | —     | —     | 134    | 1.035  | 53.7%    | Same features, LSTM(16), early-stop val_loss, threshold 0.5 (val dir 59.7% beat always-long 52.2%). Train/val/test dir 60.0%/59.7%/54.5%. Test beat always-long 51.5% and logreg 50.7%. London/NYC 56.7%/52.2%. touch 34.3% at train-median |pred| ~0.54%. Longs 90 / shorts 44. Exit session close. 2024-07 to 2026-05. |
| 17   | session_side_bce_l16_2022    | —              | 0%       | both | —     | —     | 322    | 1.124  | 54.7%    | Same net, history extended to 2022-01 (2168 sessions, split 1517/321/322). Touch level lowered to 0.20% (band to 0.40%; past the far edge still counts). Threshold 0.5 (val dir 53.3% beat always-long 52.3%). Train/val/test dir 56.2%/53.3%/55.6%. Test beat always-long 52.2% and logreg 52.2%. London/NYC 56.5%/54.7%. touch 68.0%. Longs 171 / shorts 151. Exit session close. |
| 18   | session_side_bce_l16_2022_mag | —              | 0%       | both | 80% wick | 1:1  | 322    | 1.075  | 53.7%    | Same side net, not retrained (dir stays 55.6%). Second LSTM predicts bigger-wick distance. TP is 80% of that distance, SL matches it; same-bar both counts as stop; else session close. Mean predicted wick 0.85%, mean TP 0.68%. Exits close 203 / TP 63 / SL 56. tp_reach 19.9%. Test wick MAE 0.41% loses to median baseline 0.32%. Hold-to-close equity on the same signs 1.124. Longs 171 / shorts 151. |


