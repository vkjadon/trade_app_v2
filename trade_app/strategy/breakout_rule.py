def breakout_rule(
    previous,
    candle,
):

    result = {

        "bull_score": 0,
        "bear_score": 0,

        "bull_reasons": [],
        "bear_reasons": [],

    }

    if previous is None:

        return result

    # ------------------------------------
    # Bullish Breakout
    # ------------------------------------

    if candle["High"] > previous["High"]:

        result["bull_score"] += 15

        result["bull_reasons"].append(

            "Previous High Breakout"

        )

    # ------------------------------------
    # Bearish Breakdown
    # ------------------------------------

    if candle["Low"] < previous["Low"]:

        result["bear_score"] += 15

        result["bear_reasons"].append(

            "Previous Low Breakdown"

        )

    return result