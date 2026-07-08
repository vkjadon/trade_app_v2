from datetime import timedelta
import pandas as pd

from core.application import TradingApplication
from strategy.trading_strategy import TradingStrategy
from engine.trade_engine import TradeEngine

class BacktestEngine:

    def run(self, config):

        rows = []

        app = TradingApplication()

        strategy = TradingStrategy()

        engine = TradeEngine()

        end_date = config["trading_date"]

        for i in range(config["lookback_days"]):

            trading_date = end_date - timedelta(days=i)

            cfg = config.copy()
            cfg["trading_date"] = trading_date

            try:

                result = app.run(cfg)

                df = result["data"]

                if df.empty:
                    continue

                df = strategy.generate_signals(
                    df,
                    cfg["settings"],
                )

                trades = engine.generate(df)

                if trades.empty:
                    continue

                points = trades["Points"].sum()

                wins = (trades["Points"] > 0).sum()

                losses = (trades["Points"] <= 0).sum()

                rows.append({

                    "Date": trading_date,

                    "Trades": len(trades),

                    "Wins": wins,

                    "Losses": losses,

                    "Points": round(points, 2),

                })

            except Exception:
                continue

        result = pd.DataFrame(rows)

        if not result.empty:
            result = result.sort_values("Date")
            result["Cum Points"] = result["Points"].cumsum()

        return result