from models.trade import Trade


class TradeEngine:

    def __init__(self):

        self.position = "FLAT"

        self.current_trade = None

        self.cooldown = 0

    def generate(self, df):

        trades = []

        self.position = "FLAT"
        self.current_trade = None
        self.cooldown = 0

        for _, candle in df.iterrows():

            # ------------------------------------
            # Cooldown
            # ------------------------------------

            if self.cooldown > 0:

                self.cooldown -= 1

                continue

            signal = candle["Signal"]

            # ====================================
            # FLAT
            # ====================================

            if self.position == "FLAT":

                if signal == "BUY CE":

                    self.current_trade = Trade(

                        direction="LONG",

                        entry_time=candle.name,

                        entry_price=candle["Close"],

                        confidence=candle["Confidence"],

                        reason=candle["Reason"],

                    )

                    self.position = "LONG"

                elif signal == "BUY PE":

                    self.current_trade = Trade(

                        direction="SHORT",

                        entry_time=candle.name,

                        entry_price=candle["Close"],

                        confidence=candle["Confidence"],

                        reason=candle["Reason"],

                    )

                    self.position = "SHORT"

            # ====================================
            # LONG
            # ====================================

            elif self.position == "LONG":

                if signal == "BUY PE":

                    self.current_trade.exit_time = candle.name

                    self.current_trade.exit_price = candle["Close"]

                    self.current_trade.points = (

                        self.current_trade.exit_price
                        -
                        self.current_trade.entry_price

                    )

                    trades.append(self.current_trade)

                    self.position = "SHORT"

                    self.current_trade = Trade(

                        direction="SHORT",

                        entry_time=candle.name,

                        entry_price=candle["Close"],

                        confidence=candle["Confidence"],

                        reason=candle["Reason"],

                    )

                    self.cooldown = 2

            # ====================================
            # SHORT
            # ====================================

            elif self.position == "SHORT":

                if signal == "BUY CE":

                    self.current_trade.exit_time = candle.name

                    self.current_trade.exit_price = candle["Close"]

                    self.current_trade.points = (

                        self.current_trade.entry_price
                        -
                        self.current_trade.exit_price

                    )

                    trades.append(self.current_trade)

                    self.position = "LONG"

                    self.current_trade = Trade(

                        direction="LONG",

                        entry_time=candle.name,

                        entry_price=candle["Close"],

                        confidence=candle["Confidence"],

                        reason=candle["Reason"],

                    )

                    self.cooldown = 2

        # ------------------------------------
        # Close Last Position
        # ------------------------------------

        if self.current_trade is not None:

            last = df.iloc[-1]

            self.current_trade.exit_time = last.name

            self.current_trade.exit_price = last["Close"]

            if self.current_trade.direction == "LONG":

                self.current_trade.points = (

                    self.current_trade.exit_price
                    -
                    self.current_trade.entry_price

                )

            else:

                self.current_trade.points = (

                    self.current_trade.entry_price
                    -
                    self.current_trade.exit_price

                )

            trades.append(self.current_trade)

        return trades