from datetime import time


class TradingStrategy:

    def __init__(self):
        self.last_signal = "WAIT"

    def generate_signals(self, df, settings):

        if settings["strategy"] == "Classic ORB":
            return self.classic_orb(df)

        if settings["strategy"] == "Smart ORB":
            return self.smart_orb(df)

        return df

    def classic_orb(self, df):

        self.last_signal = "WAIT"

        df = df.copy()

        df["Signal"] = "WAIT"
        df["Reason"] = ""

        for i in range(1, len(df)):

            current = df.iloc[i]
            previous = df.iloc[i - 1]

            signal = "WAIT"

            current_time = current.name.time()

            # ----------------------------------
            # Time Filter
            # ----------------------------------

            if current_time < time(9, 30):
                continue

            if current_time >= time(15, 15):
                continue

            # ----------------------------------
            # Trend
            # ----------------------------------

            ce_trend = (
                current["Close"] > current["EMA20"]
                and current["EMA20"] > previous["EMA20"]
            )

            pe_trend = (
                current["Close"] < current["EMA20"]
                and current["EMA20"] < previous["EMA20"]
            )

            # ----------------------------------
            # RSI
            # ----------------------------------

            ce_momentum = current["RSI"] > 55
            pe_momentum = current["RSI"] < 45

            # ----------------------------------
            # MACD
            # ----------------------------------

            ce_macd = current["MACD"] > current["MACDSignal"]
            pe_macd = current["MACD"] < current["MACDSignal"]

            # ----------------------------------
            # Breakout
            # ----------------------------------

            ORB_THRESHOLD = 60

            orb_range = current["ORB_High"] - current["ORB_Low"]

            if orb_range <= ORB_THRESHOLD:
                ce_breakout = current["Close"] > current["ORB_High"]
                pe_breakout = current["Close"] < current["ORB_Low"]
            else:
                ce_breakout = current["High"] > previous["High"]
                pe_breakout = current["Low"] < previous["Low"]

            # ----------------------------------
            # Candle
            # ----------------------------------

            body = abs(current["Close"] - current["Open"])
            range_ = current["High"] - current["Low"]

            strong_body = range_ > 0 and body / range_ >= 0.6

            ce_candle = current["Close"] > current["Open"] and strong_body
            pe_candle = current["Close"] < current["Open"] and strong_body

            # ----------------------------------
            # BUY Signals
            # ----------------------------------

            if (
                ce_trend
                and ce_momentum
                and ce_macd
                and ce_breakout
                and ce_candle
            ):

                signal = "BUY CE"
                reasons = ["All Conditions Satisfied"]

            elif (
                pe_trend
                and pe_momentum
                and pe_macd
                and pe_breakout
                and pe_candle
            ):

                signal = "BUY PE"
                reasons = ["All Conditions Satisfied"]

            else:

                reasons = []

                if not (ce_trend or pe_trend):
                    reasons.append("❌ Trend")

                if not (ce_momentum or pe_momentum):
                    reasons.append("❌ RSI")

                if not (ce_macd or pe_macd):
                    reasons.append("❌ MACD")

                if not (ce_breakout or pe_breakout):
                    reasons.append("❌ Breakout")

                if not (ce_candle or pe_candle):
                    reasons.append("❌ Strong Candle")

            # ----------------------------------
            # Duplicate Signal
            # ----------------------------------

            if signal in ["BUY CE", "BUY PE"]:

                if signal == self.last_signal:
                    reasons = ["Duplicate Signal"]

                else:
                    self.last_signal = signal
        
        
            if signal in ["BUY CE", "BUY PE"]:
                self.last_signal = signal

            # ----------------------------------
            # Store
            # ----------------------------------

            df.at[df.index[i], "Signal"] = signal
            df.at[df.index[i], "Reason"] = "\n".join(reasons)

        return df
    
    
    def smart_orb(self, df,):

        self.last_signal = "WAIT"

        df = df.copy()

        df["Signal"] = "WAIT"
        df["Reason"] = ""

        for i in range(1, len(df)):

            current = df.iloc[i]
            previous = df.iloc[i - 1]

            signal = "WAIT"

            current_time = current.name.time()

            # ----------------------------------
            # Time Filter
            # ----------------------------------

            if current_time < time(9, 30):
                continue

            if current_time >= time(15, 15):
                continue

            # ----------------------------------
            # Trend
            # ----------------------------------

            ce_trend = (
                current["Close"] > current["EMA20"]
                and current["EMA20"] > previous["EMA20"]
            )

            pe_trend = (
                current["Close"] < current["EMA20"]
                and current["EMA20"] < previous["EMA20"]
            )

            # ----------------------------------
            # RSI
            # ----------------------------------

            ce_momentum = current["RSI"] > 55
            pe_momentum = current["RSI"] < 45

            # ----------------------------------
            # MACD
            # ----------------------------------

            ce_macd = current["MACD"] > current["MACDSignal"]
            pe_macd = current["MACD"] < current["MACDSignal"]

            # ----------------------------------
            # Volume
            # ----------------------------------

            ce_volume_ok = (current["CE_Volume"] > current["CE_Volume_SMA20"])

            pe_volume_ok = (current["PE_Volume"] > current["PE_Volume_SMA20"])

            # ----------------------------------
            # VWAP
            # ----------------------------------

            # ce_vwap = current["Close"] > current["VWAP"]
            # pe_vwap = current["Close"] < current["VWAP"]
            
            ce_vwap_ok = (current["CE_Close"] > current["CE_VWAP"])
            pe_vwap_ok = (current["PE_Close"] > current["PE_VWAP"])

            # ----------------------------------
            # Breakout
            # ----------------------------------

            ORB_THRESHOLD = 60

            orb_range = current["ORB_High"] - current["ORB_Low"]

            if orb_range <= ORB_THRESHOLD:
                ce_breakout = current["Close"] > current["ORB_High"]
                pe_breakout = current["Close"] < current["ORB_Low"]
            else:
                ce_breakout = current["High"] > previous["High"]
                pe_breakout = current["Low"] < previous["Low"]

            # ----------------------------------
            # Candle
            # ----------------------------------

            body = abs(current["Close"] - current["Open"])
            range_ = current["High"] - current["Low"]

            strong_body = range_ > 0 and body / range_ >= 0.6

            ce_candle = current["Close"] > current["Open"] and strong_body
            pe_candle = current["Close"] < current["Open"] and strong_body

            # ----------------------------------
            # BUY Signals
            # ----------------------------------

            if (
                ce_trend
                and ce_momentum
                and ce_macd
                and ce_breakout
                and ce_candle
                # and ce_volume_ok
                and ce_vwap_ok
            ):

                signal = "BUY CE"
                reasons = ["All Conditions Satisfied"]

            elif (
                pe_trend
                and pe_momentum
                and pe_macd
                and pe_breakout
                and pe_candle
                # and pe_volume_ok
                and pe_vwap_ok
            ):

                signal = "BUY PE"
                reasons = ["All Conditions Satisfied"]

            else:

                reasons = []

                if not (ce_trend or pe_trend):
                    reasons.append("❌ Trend")

                if not (ce_momentum or pe_momentum):
                    reasons.append("❌ RSI")

                if not (ce_macd or pe_macd):
                    reasons.append("❌ MACD")

                if not (ce_breakout or pe_breakout):
                    reasons.append("❌ Breakout")

                if not (ce_candle or pe_candle):
                    reasons.append("❌ Strong Candle")
 
                # if not (ce_volume_ok or pe_volume_ok):
                #     reasons.append("❌ Volume")
    
                if not (ce_vwap_ok or pe_vwap_ok):
                    reasons.append("❌ VWAP")
    
            # ----------------------------------
            # Duplicate Signal
            # ----------------------------------

            if signal in ["BUY CE", "BUY PE"]:

                if signal == self.last_signal:
                    reasons = ["Duplicate Signal"]

                else:
                    self.last_signal = signal
        
        
            if signal in ["BUY CE", "BUY PE"]:
                self.last_signal = signal

            # ----------------------------------
            # Store
            # ----------------------------------

            df.at[df.index[i], "Signal"] = signal
            df.at[df.index[i], "Reason"] = "\n".join(reasons)

        return df
    
    