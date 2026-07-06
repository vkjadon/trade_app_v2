import pandas as pd
from datetime import time


class TradeEngine:

    def generate(self, df):

        trades = []

        trade = None

        for i in range(1, len(df)):

            candle = df.iloc[i]
            previous = df.iloc[i - 1]
            current_time = candle.name.time()

            # --------------------------------------------------
            # 1. Exit Existing Trade
            # --------------------------------------------------

            if trade is not None:

                exit_trade = False

                if trade["Signal"] == "BUY CE":

                    if candle["Low"] <= trade["SL"]:
                        exit_price = trade["SL"]
                        exit_reason = "SL"
                        exit_trade = True

                    elif candle["High"] >= trade["Target"]:
                        exit_price = trade["Target"]
                        exit_reason = "TARGET"
                        exit_trade = True

                else:

                    if candle["High"] >= trade["SL"]:
                        exit_price = trade["SL"]
                        exit_reason = "SL"
                        exit_trade = True

                    elif candle["Low"] <= trade["Target"]:
                        exit_price = trade["Target"]
                        exit_reason = "TARGET"
                        exit_trade = True

                if not exit_trade and current_time >= time(15, 15):
                    exit_price = candle["Close"]
                    exit_reason = "EOD"
                    exit_trade = True

                if exit_trade:

                    trade["Exit Time"] = candle.name
                    trade["Exit"] = round(exit_price, 2)
                    trade["Exit Reason"] = exit_reason

                    if trade["Signal"] == "BUY CE":
                        trade["Points"] = round(exit_price - trade["Entry"], 2)
                    else:
                        trade["Points"] = round(trade["Entry"] - exit_price, 2)

                    trades.append(trade)
                    trade = None

            # --------------------------------------------------
            # 2. Open New Trade (same candle allowed)
            # --------------------------------------------------

            if trade is None and candle["Signal"] in ["BUY CE", "BUY PE"]:

                entry = candle["Close"]

                if candle["Signal"] == "BUY CE":

                    sl = previous["Low"] - 2
                    risk = entry - sl
                    target = entry + (2 * risk)

                else:

                    sl = previous["High"] + 2
                    risk = sl - entry
                    target = entry - (2 * risk)

                trade = {
                    "Signal": candle["Signal"],
                    "Entry Time": candle.name,
                    "Entry": round(entry, 2),
                    "SL": round(sl, 2),
                    "Target": round(target, 2),
                    "Reason": candle["Reason"],
                }
        
        # --------------------------------------------------
        # Close Last Open Trade
        # --------------------------------------------------

        if trade is not None:

            last = df.iloc[-1]

            trade["Exit Time"] = last.name
            trade["Exit"] = round(last["Close"], 2)
            trade["Exit Reason"] = "EOD"

            if trade["Signal"] == "BUY CE":
                trade["Points"] = round(
                    trade["Exit"] - trade["Entry"], 2
                )
            else:
                trade["Points"] = round(
                    trade["Entry"] - trade["Exit"], 2
                )

            trades.append(trade)
    
        return pd.DataFrame(trades)