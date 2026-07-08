from datetime import datetime, timedelta, time

import pandas as pd

from config.market import (
    MARKET_OPEN,
    MARKET_CLOSE,
)

from data.kite_client import get_kite
from data.instrument_manager import InstrumentManager


class MarketData:

    def __init__(self):

        self.kite = get_kite()

        self.instrument_manager = InstrumentManager()

    # --------------------------------------------------
    # Keep only trading hours
    # --------------------------------------------------

    def trim_market_hours(self, df):

        if df.empty:
            return df

        return df.between_time(
            MARKET_OPEN,
            MARKET_CLOSE,
        )

    # --------------------------------------------------
    # Historical Data
    # --------------------------------------------------

    def get_history_by_token(

        self,

        instrument_token,

        interval="5minute",

        trading_date=None,

        lookback_days=5,

        oi=True,

    ):

        # ----------------------------------------
        # Download Window
        # ----------------------------------------

        if trading_date is None:

            to_date = datetime.now()

            from_date = to_date - timedelta(days=lookback_days)

        else:

            end_of_day = datetime.combine(

                trading_date,

                time(23, 59, 59),

            )

            from_date = end_of_day - timedelta(

                days=lookback_days

            )

            to_date = end_of_day

        # ----------------------------------------

        candles = self.kite.historical_data(

            instrument_token=instrument_token,

            from_date=from_date,

            to_date=to_date,

            interval=interval,

            oi=oi,

        )

        df = pd.DataFrame(candles)

        if df.empty:

            return df

        df.rename(

            columns={

                "date": "Datetime",

                "open": "Open",

                "high": "High",

                "low": "Low",

                "close": "Close",

                "volume": "Volume",

                "oi": "OI",
                
                "strike": "strike",

            },

            inplace=True,

        )

        df["Datetime"] = pd.to_datetime(

            df["Datetime"]

        )

        df.set_index(

            "Datetime",

            inplace=True,

        )

        df.sort_index(inplace=True)

        # ----------------------------------------

        df = self.trim_market_hours(df)

        # ----------------------------------------

        return df

    # --------------------------------------------------
    # Spot Data
    # --------------------------------------------------

    def get_spot_data(

        self,

        index_name,

        interval="5minute",

        trading_date=None,

        lookback_days=5,

    ):

        token = self.instrument_manager.get_spot_token(

            index_name

        )

        return self.get_history_by_token(

            instrument_token=token,

            interval=interval,

            trading_date=trading_date,

            lookback_days=lookback_days,

        )

    # --------------------------------------------------
    # Option Data
    # --------------------------------------------------

    # --------------------------------------------------
    # LTP
    # --------------------------------------------------

    def get_ltp(self, index_name):

        quote_symbol = (

            self.instrument_manager.get_spot_quote_symbol(

                index_name

            )

        )

        data = self.kite.ltp(

            quote_symbol

        )

        return data[quote_symbol]["last_price"]

    # --------------------------------------------------
    # Quote
    # --------------------------------------------------

    def get_quote(self, index_name):

        quote_symbol = (

            self.instrument_manager.get_spot_quote_symbol(

                index_name

            )

        )

        data = self.kite.quote(

            quote_symbol

        )

        return data[quote_symbol]
    
    def get_option_data_by_token(
        self,
        instrument_token,
        interval="5minute",
        trading_date=None,
        lookback_days=5,
    ):

        return self.get_history_by_token(
            instrument_token=instrument_token,
            interval=interval,
            trading_date=trading_date,
            lookback_days=lookback_days,
        )