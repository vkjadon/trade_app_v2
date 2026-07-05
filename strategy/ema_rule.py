def ema_rule(
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
    # EMA disabled
    # ------------------------------------------

    if not settings["ema"]:

        return result

    if "EMA20" not in candle.index:

        return result

    if previous is None:

        return result

    # ------------------------------------------
    # Bullish
    # ------------------------------------------

    if candle["Close"] > candle["EMA20"]:

        result["bull_score"] += 20

        result["bull_reasons"].append(

            "Close above EMA20"

        )

    if candle["EMA20"] > previous["EMA20"]:

        result["bull_score"] += 10

        result["bull_reasons"].append(

            "EMA Rising"

        )

    # ------------------------------------------
    # Bearish
    # ------------------------------------------

    if candle["Close"] < candle["EMA20"]:

        result["bear_score"] += 20

        result["bear_reasons"].append(

            "Close below EMA20"

        )

    if candle["EMA20"] < previous["EMA20"]:

        result["bear_score"] += 10

        result["bear_reasons"].append(

            "EMA Falling"

        )

    return result