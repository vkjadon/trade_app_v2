from config.strategy import (
    RSI_BULL_LEVEL,
    RSI_BEAR_LEVEL,
    RSI_SCORE,
)

import pandas as pd


def rsi_rule(
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

    if not settings["rsi"]:

        return result

    if "RSI" not in candle.index:

        return result

    rsi = candle["RSI"]

    if pd.isna(rsi):

        return result

    # ------------------------------------------
    # Bullish
    # ------------------------------------------

    if rsi >= RSI_BULL_LEVEL:

        result["bull_score"] += RSI_SCORE

        result["bull_reasons"].append(

            f"RSI > {RSI_BULL_LEVEL}"

        )

    # ------------------------------------------
    # Bearish
    # ------------------------------------------

    if rsi <= RSI_BEAR_LEVEL:

        result["bear_score"] += RSI_SCORE

        result["bear_reasons"].append(

            f"RSI < {RSI_BEAR_LEVEL}"

        )

    # ------------------------------------------
    # RSI Momentum
    # ------------------------------------------

    if previous is not None:

        prev_rsi = previous["RSI"]

        if not pd.isna(prev_rsi):

            if rsi > prev_rsi:

                result["bull_score"] += 5

                result["bull_reasons"].append(

                    "RSI Rising"

                )

            elif rsi < prev_rsi:

                result["bear_score"] += 5

                result["bear_reasons"].append(

                    "RSI Falling"

                )

    return result