from datetime import time


def time_rule(candle):

    result = {

        "allowed": True,

        "bull_score": 0,
        "bear_score": 0,

        "bull_reasons": [],
        "bear_reasons": [],

    }

    # ------------------------------------------
    # Get candle time
    # ------------------------------------------

    current_time = candle.name.time()

    # ------------------------------------------
    # Ignore Opening Noise
    # ------------------------------------------

    if current_time < time(9, 15):

        result["allowed"] = False

        return result

    # ------------------------------------------
    # Ignore Last 05 Minutes
    # ------------------------------------------

    if current_time >= time(15, 15):

        result["allowed"] = False

        return result

    return result