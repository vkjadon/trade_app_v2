import pandas as pd


class TradeEngine:

    def generate(self, df):

        trades = []

        current_trade = None

        for index, candle in df.iterrows():

            signal = candle["Signal"]

            # ----------------------------
            # Open Trade
            # ----------------------------

            if current_trade is None:

                if signal in ["BUY CE", "BUY PE"]:

                    current_trade = {
                        "Signal": signal,
                        "Entry Time": index,
                        "Entry": candle["Close"],
                        "Reason": candle["Reason"],
                    }

                continue

            # ----------------------------
            # Reverse Trade
            # ----------------------------

            if signal != current_trade["Signal"] and signal in ["BUY CE", "BUY PE"]:

                current_trade["Exit Time"] = index
                current_trade["Exit"] = candle["Close"]

                if current_trade["Signal"] == "BUY CE":
                    current_trade["Points"] = (
                        current_trade["Exit"] - current_trade["Entry"]
                    )
                else:
                    current_trade["Points"] = (
                        current_trade["Entry"] - current_trade["Exit"]
                    )

                trades.append(current_trade)

                current_trade = {
                    "Signal": signal,
                    "Entry Time": index,
                    "Entry": candle["Close"],
                    "Reason": candle["Reason"],
                }

        # ----------------------------
        # Close Last Trade
        # ----------------------------

        if current_trade is not None:

            last = df.iloc[-1]

            current_trade["Exit Time"] = last.name
            current_trade["Exit"] = last["Close"]

            if current_trade["Signal"] == "BUY CE":
                current_trade["Points"] = (
                    current_trade["Exit"] - current_trade["Entry"]
                )
            else:
                current_trade["Points"] = (
                    current_trade["Entry"] - current_trade["Exit"]
                )

            trades.append(current_trade)

        return pd.DataFrame(trades)