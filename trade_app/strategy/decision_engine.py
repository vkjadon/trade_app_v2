class DecisionEngine:

    BUY_THRESHOLD = 80

    REVERSAL_MARGIN = 20

    def decide(

        self,

        bull_score,

        bear_score,

    ):

        result = {

            "signal": "WAIT",

            "direction": "NONE",

            "confidence": "LOW",

        }

        # ---------------------------------------
        # Bullish Decision
        # ---------------------------------------

        if (

            bull_score >= self.BUY_THRESHOLD

            and

            bull_score >= bear_score + self.REVERSAL_MARGIN

        ):

            result["signal"] = "BUY CE"

            result["direction"] = "LONG"

        # ---------------------------------------
        # Bearish Decision
        # ---------------------------------------

        elif (

            bear_score >= self.BUY_THRESHOLD

            and

            bear_score >= bull_score + self.REVERSAL_MARGIN

        ):

            result["signal"] = "BUY PE"

            result["direction"] = "SHORT"

        # ---------------------------------------
        # Confidence
        # ---------------------------------------

        score = max(

            bull_score,

            bear_score,

        )

        if score >= 90:

            result["confidence"] = "VERY HIGH"

        elif score >= 80:

            result["confidence"] = "HIGH"

        elif score >= 70:

            result["confidence"] = "MEDIUM"

        else:

            result["confidence"] = "LOW"

        return result