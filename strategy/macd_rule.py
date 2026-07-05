from config.strategy import (
    MACD_SCORE,
)

import pandas as pd


def macd_rule(
    previous,
    candle,
    settings,
):

    result = {

        "bull_score": 0,
        "bear_score": 0,

        "bull_reasons": [],
        "bear_reasons": [],

    }

    # ------------------------------------------
    # Disabled
    # ------------------------------------------

    if not settings["macd"]:

        return result

    required = [

        "MACD",
        "Signal",
        "Histogram",

    ]

    if not all(col in candle.index for col in required):

        return result

    macd = candle["MACD"]
    signal = candle["Signal"]
    hist = candle["Histogram"]

    if pd.isna(macd) or pd.isna(signal):

        return result

    # ------------------------------------------
    # Bullish Crossover
    # ------------------------------------------

    if macd > signal:

        result["bull_score"] += MACD_SCORE

        result["bull_reasons"].append(

            "MACD Bullish"

        )

    # ------------------------------------------
    # Bearish Crossover
    # ------------------------------------------

    if macd < signal:

        result["bear_score"] += MACD_SCORE

        result["bear_reasons"].append(

            "MACD Bearish"

        )

    # ------------------------------------------
    # Histogram Momentum
    # ------------------------------------------

    if previous is not None:

        prev_hist = previous["Histogram"]

        if not pd.isna(prev_hist):

            if hist > prev_hist:

                result["bull_score"] += 5

                result["bull_reasons"].append(

                    "MACD Momentum Rising"

                )

            elif hist < prev_hist:

                result["bear_score"] += 5

                result["bear_reasons"].append(

                    "MACD Momentum Falling"

                )

    return result