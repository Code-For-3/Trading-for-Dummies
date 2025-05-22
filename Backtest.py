import pandas as pd

def backtest_with_rr_exit(data, initial_cash=1000, risk_per_trade=0.01, leverage=1, rr_ratio=2, stop_pct=0.01):
    in_position = False
    position_type = None
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

        if not in_position and signal in [1, -1]:
            entry_price = price
            risk_amount = cash * risk_per_trade * leverage
            stop_loss = stop_pct * price
            position_size = risk_amount / stop_loss
            position_type = 'long' if signal == 1 else 'short'
            in_position = True

            tp_price = (
                entry_price + rr_ratio * stop_loss if position_type == 'long'
                else entry_price - rr_ratio * stop_loss
            )
            sl_price = (
                entry_price - stop_loss if position_type == 'long'
                else entry_price + stop_loss
            )

            trade_log.append({
                'timestamp': timestamp,
                'action': 'entry',
                'side': position_type,
                'entry_price': entry_price,
                'tp_price': tp_price,
                'sl_price': sl_price,
                'size': position_size
            })

        elif in_position:
            hit_tp = price >= tp_price if position_type == 'long' else price <= tp_price
            hit_sl = price <= sl_price if position_type == 'long' else price >= sl_price

            if hit_tp or hit_sl:
                exit_price = price
                pnl = (exit_price - entry_price) * position_size if position_type == 'long' else (entry_price - exit_price) * position_size
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

    if len(data) > 0:
        equity_curve.append((data.index[-1], cash))

    equity_series = pd.Series(
        [val for (_, val) in equity_curve],
        index=pd.to_datetime([ts for (ts, _) in equity_curve])
    )

    return equity_series, trade_log
