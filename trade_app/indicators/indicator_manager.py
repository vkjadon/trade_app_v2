from indicators import atr, ema, macd
from indicators import volume
from indicators import (
    vwap,
)
from indicators import rsi

class IndicatorManager:

    def calculate(
        self,
        df,
        settings,
    ):

        if settings.get("ema", True):

            df = ema.calculate(df)

        if settings.get("rsi", True):

            df = rsi.calculate(df)

            print(
                df[
                    [
                        "Close",
                        "RSI",
                    ]
                ].head(20)
            )

        if settings.get("macd", True):

            df = macd.calculate(df)

        if settings.get("vwap", False):

            df = vwap.calculate(df)

        if settings.get("volume", False):

            df = volume.calculate(df)

        # ATR is always calculated.
        # It will be used later for stop loss.

        df = atr.calculate(df)
        
        # ---------------------------------------
        # Smart ORB : Option Volume
        # ---------------------------------------

        if "CE_Volume" in df.columns:

            df["CE_Volume_SMA20"] = (
                df["CE_Volume"]
                .rolling(window=20, min_periods=1)
                .mean()
            )

        if "PE_Volume" in df.columns:

            df["PE_Volume_SMA20"] = (
                df["PE_Volume"]
                .rolling(window=20, min_periods=1)
                .mean()
            )
        return df