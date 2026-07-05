from indicators import (
    ema,
    rsi,
    macd,
    vwap,
    atr,
    volume,
)


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

        return df