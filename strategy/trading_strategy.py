from datetime import time


class TradingStrategy:

    def __init__(self):
        self.last_signal = "WAIT"

    def generate_signals(self, df, settings):

        df = df.copy()

        # Output Columns
        df["Signal"] = "WAIT"
        df["Reason"] = ""

        # Process candles
        for i in range(1, len(df)):

            current = df.iloc[i]
            previous = df.iloc[i - 1]
            
            signal = "WAIT"
            reasons = []

            # ----------------------------------
            # Time Filter (only check for now)
            # ----------------------------------

            current_time = current.name.time()

            if current_time < time(9, 30):
                df.at[df.index[i], "Signal"] = signal
                continue

            if current_time >= time(15, 15):
                df.at[df.index[i], "Signal"] = signal
                continue

            

            # ----------------------------------
            # CALL Trend
            # ----------------------------------

            ce_trend = (
                current["Close"] > current["EMA20"]
                and current["EMA20"] > previous["EMA20"]
            )

            # ----------------------------------
            # PUT Trend
            # ----------------------------------

            pe_trend = (
                current["Close"] < current["EMA20"]
                and current["EMA20"] < previous["EMA20"]
            )
            
            ce_momentum = current["RSI"] > 55
            pe_momentum = current["RSI"] < 45

            if ce_trend and ce_momentum:
                signal = "CE Trend"
                reasons.append("Price > EMA20")
                reasons.append("EMA20 Rising")
                reasons.append("RSI > 55")

            elif pe_trend and pe_momentum:
                signal = "PE Trend"
                reasons.append("Price < EMA20")
                reasons.append("EMA20 Falling")
                reasons.append("RSI < 45")
        
            # ----------------------------------
            # Store
            # ----------------------------------

            df.at[df.index[i], "Signal"] = signal
            df.at[df.index[i], "Reason"] = "\n".join(reasons)
            
        return df