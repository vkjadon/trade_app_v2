from datetime import datetime


class OptionDataService:

    def get_atm_strike(self, spot_price):

        return int(round(spot_price / 50.0) * 50)

    def get_expiry(self, kite):

        instruments = kite.instruments("NFO")

        expiries = sorted({
            ins["expiry"]
            for ins in instruments
            if ins["name"] == "NIFTY"
            and ins["segment"] == "NFO-OPT"
        })

        return expiries[0]   
      
    def get_symbol(self, kite, spot_price, option_type):

        strike = self.get_atm_strike(spot_price)

        expiry = self.get_expiry(kite)

        instruments = kite.instruments("NFO")

        for ins in instruments:

            if (
                ins["name"] == "NIFTY"
                and ins["expiry"] == expiry
                and ins["strike"] == strike
                and ins["instrument_type"] == option_type
            ):
                return ins["tradingsymbol"], ins["instrument_token"]

        return None, None