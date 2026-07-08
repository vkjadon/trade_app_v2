def bullish_rule(candle, settings):

    reasons = []

    # ----------------------------------
    # EMA
    # ----------------------------------

    if settings.get("ema", False):

        if "EMA20" not in candle.index:
            return False, []

        if candle["Close"] <= candle["EMA20"]:
            return False, []

        reasons.append("EMA")

    # ----------------------------------
    # RSI
    # ----------------------------------

    if settings.get("rsi", False):

        if "RSI" not in candle.index:
            return False, []

        if candle["RSI"] < 55:
            return False, []

        reasons.append("RSI")

    # ----------------------------------
    # MACD
    # ----------------------------------

    if settings.get("macd", False):

        if (
            "MACD_12_26_9" not in candle.index
            or
            "MACDs_12_26_9" not in candle.index
        ):
            return False, []

        if candle["MACD_12_26_9"] <= candle["MACDs_12_26_9"]:
            return False, []

        reasons.append("MACD")

    return True, reasons


# ======================================================


def bearish_rule(candle, settings):

    reasons = []

    # ----------------------------------
    # EMA
    # ----------------------------------

    if settings.get("ema", False):

        if "EMA20" not in candle.index:
            return False, []

        if candle["Close"] >= candle["EMA20"]:
            return False, []

        reasons.append("EMA")

    # ----------------------------------
    # RSI
    # ----------------------------------

    if settings.get("rsi", False):

        if "RSI" not in candle.index:
            return False, []

        if candle["RSI"] > 45:
            return False, []

        reasons.append("RSI")

    # ----------------------------------
    # MACD
    # ----------------------------------

    if settings.get("macd", False):

        if (
            "MACD_12_26_9" not in candle.index
            or
            "MACDs_12_26_9" not in candle.index
        ):
            return False, []

        if candle["MACD_12_26_9"] >= candle["MACDs_12_26_9"]:
            return False, []

        reasons.append("MACD")

    return True, reasons