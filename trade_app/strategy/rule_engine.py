from trade_app.config.strategy import (
    BUY_THRESHOLD,
    WATCH_THRESHOLD,
)

from trade_app.strategy.ema_rule import ema_rule
from trade_app.strategy.rsi_rule import rsi_rule
from trade_app.strategy.macd_rule import macd_rule
from trade_app.strategy.candle_rule import candle_rule
from trade_app.strategy.breakout_rule import breakout_rule
from trade_app.strategy.time_rule import time_rule


class RuleEngine:

    def evaluate(
        self,
        candle,
        previous,
        candle_number,
        settings,
    ):

        score = 0

        reasons = []

        bullish = 0

        bearish = 0

        # =====================================================
        # TIME FILTER
        # =====================================================

        result = time_rule(
            candle.name,
            candle_number,
        )

        if not result["passed"]:

            return {

                "signal": "WAIT",

                "score": 0,

                "confidence": 0,

                "direction": None,

                "reasons": result["reasons"],

            }

        score += result["score"]

        reasons.extend(result["reasons"])

        # =====================================================
        # EMA
        # =====================================================

        if settings.get("ema", True):

            result = ema_rule(
                candle,
                previous,
            )

            if result["passed"]:

                score += result["score"]

                reasons.extend(result["reasons"])

                if result["direction"] == "BULLISH":

                    bullish += 1

                elif result["direction"] == "BEARISH":

                    bearish += 1

        # =====================================================
        # RSI
        # =====================================================

        if settings.get("rsi", True):

            result = rsi_rule(
                candle,
                previous,
            )

            if result["passed"]:

                score += result["score"]

                reasons.extend(result["reasons"])

                if result["direction"] == "BULLISH":

                    bullish += 1

                elif result["direction"] == "BEARISH":

                    bearish += 1

        # =====================================================
        # MACD
        # =====================================================

        if settings.get("macd", True):

            result = macd_rule(
                candle,
                previous,
            )

            if result["passed"]:

                score += result["score"]

                reasons.extend(result["reasons"])

                if result["direction"] == "BULLISH":

                    bullish += 1

                elif result["direction"] == "BEARISH":

                    bearish += 1

        # =====================================================
        # CANDLE
        # =====================================================

        result = candle_rule(
            candle,
        )

        if result["passed"]:

            score += result["score"]

            reasons.extend(result["reasons"])

            if result["direction"] == "BULLISH":

                bullish += 1

            elif result["direction"] == "BEARISH":

                bearish += 1

        # =====================================================
        # BREAKOUT
        # =====================================================

        result = breakout_rule(
            candle,
            previous,
        )

        if result["passed"]:

            score += result["score"]

            reasons.extend(result["reasons"])

            if result["direction"] == "BULLISH":

                bullish += 1

            elif result["direction"] == "BEARISH":

                bearish += 1

        # =====================================================
        # FINAL DECISION
        # =====================================================

        signal = "WAIT"

        direction = None

        if bullish > bearish:

            direction = "BULLISH"

            if score >= BUY_THRESHOLD:

                signal = "BUY CE"

            elif score >= WATCH_THRESHOLD:

                signal = "WATCH"

        elif bearish > bullish:

            direction = "BEARISH"

            if score >= BUY_THRESHOLD:

                signal = "BUY PE"

            elif score >= WATCH_THRESHOLD:

                signal = "WATCH"

        confidence = round(score)

        return {

            "signal": signal,

            "score": score,

            "confidence": confidence,

            "direction": direction,

            "reasons": reasons,

        }