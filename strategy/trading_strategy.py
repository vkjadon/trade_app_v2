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

            ce_macd = current["MACD"] > current["MACDSignal"]
            pe_macd = current["MACD"] < current["MACDSignal"]

            ce_breakout = current["High"] > previous["High"]
            pe_breakout = current["Low"] < previous["Low"]

            body = abs(current["Close"] - current["Open"])
            range_ = current["High"] - current["Low"]

            strong_body = range_ > 0 and body / range_ >= 0.6

            ce_candle = (current["Close"] > current["Open"] and strong_body)
            pe_candle = (current["Close"] < current["Open"] and strong_body)
            
            if ce_trend and ce_momentum and ce_macd and ce_breakout and ce_candle:
                signal = "BUY CE"
                reasons.append("Price > EMA20")
                reasons.append("EMA20 Rising")
                reasons.append("RSI > 55")
                reasons.append("MACD Bullish")
                reasons.append("Previous High Breakout")
                reasons.append("Strong Bull Candle")

            elif pe_trend and pe_momentum and pe_macd and pe_breakout and pe_candle:
                signal = "BUY PE"
                reasons.append("Price < EMA20")
                reasons.append("EMA20 Falling")
                reasons.append("RSI < 45")
                reasons.append("MACD Bearish")
                reasons.append("Previous Low Breakout")
                reasons.append("Strong Bear Candle")

            
            
            # ----------------------------------
            # Store
            # ----------------------------------

            df.at[df.index[i], "Signal"] = signal
            df.at[df.index[i], "Reason"] = "\n".join(reasons)
            
        return df