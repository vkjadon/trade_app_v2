def candle_rule(
    previous,
    candle,
):

    result = {

        "bull_score": 0,
        "bear_score": 0,

        "bull_reasons": [],
        "bear_reasons": [],

    }

    # ------------------------------------------
    # Candle Measurements
    # ------------------------------------------

    body = abs(
        candle["Close"] - candle["Open"]
    )

    total = candle["High"] - candle["Low"]

    if total <= 0:

        return result

    upper_wick = candle["High"] - max(

        candle["Open"],

        candle["Close"]

    )

    lower_wick = min(

        candle["Open"],

        candle["Close"]

    ) - candle["Low"]

    body_ratio = body / total

    # ------------------------------------------
    # Strong Bull Candle
    # ------------------------------------------

    if (

        candle["Close"] > candle["Open"]

        and

        body_ratio >= 0.70

    ):

        result["bull_score"] += 20

        result["bull_reasons"].append(

            "Strong Bull Candle"

        )

    # ------------------------------------------
    # Strong Bear Candle
    # ------------------------------------------

    if (

        candle["Close"] < candle["Open"]

        and

        body_ratio >= 0.70

    ):

        result["bear_score"] += 20

        result["bear_reasons"].append(

            "Strong Bear Candle"

        )

    # ------------------------------------------
    # Bullish Rejection
    # ------------------------------------------

    if (

        lower_wick > body * 2

        and

        candle["Close"] > candle["Open"]

    ):

        result["bull_score"] += 10

        result["bull_reasons"].append(

            "Bullish Rejection"

        )

    # ------------------------------------------
    # Bearish Rejection
    # ------------------------------------------

    if (

        upper_wick > body * 2

        and

        candle["Close"] < candle["Open"]

    ):

        result["bear_score"] += 10

        result["bear_reasons"].append(

            "Bearish Rejection"

        )

    return result