from pathlib import Path
from datetime import date

import pandas as pd

from config.symbols import SPOT_INDICES

from config.settings import (
    CACHE_FOLDER,
    INSTRUMENT_FILE,
)

from data.kite_client import get_kite


class InstrumentManager:

    def __init__(self):

        Path(CACHE_FOLDER).mkdir(
            exist_ok=True
        )

        self.kite = get_kite()

        self.df = None

    # --------------------------------------------------
    # Download Instruments
    # --------------------------------------------------

    def download(self):

        self.df = pd.DataFrame(
            self.kite.instruments()
        )

        self.df.to_csv(
            INSTRUMENT_FILE,
            index=False
        )

        return self.df

    # --------------------------------------------------
    # Load Instruments
    # --------------------------------------------------

    def load(self):

        if self.df is not None:
            return self.df

        if Path(INSTRUMENT_FILE).exists():

            self.df = pd.read_csv(
                INSTRUMENT_FILE
            )

        else:

            self.download()

        return self.df

    # --------------------------------------------------
    # Refresh
    # --------------------------------------------------

    def refresh(self):

        return self.download()

    # --------------------------------------------------
    # Available Exchanges
    # --------------------------------------------------

    def get_exchanges(self):

        df = self.load()

        return sorted(
            df["exchange"]
            .dropna()
            .unique()
        )

    # --------------------------------------------------
    # Indices
    # --------------------------------------------------

    def get_indices(self):

        return [
            "NIFTY",
            "BANKNIFTY",
            "FINNIFTY",
            "MIDCPNIFTY",
            "SENSEX",
        ]

    # --------------------------------------------------
    # Expiries
    # --------------------------------------------------

    def get_expiries(self, index_name):

        df = self.load()

        option_df = df[
            (df["name"] == index_name)
            &
            (df["segment"] == "NFO-OPT")
        ]

        expiries = (
            option_df["expiry"]
            .dropna()
            .unique()
            .tolist()
        )

        expiries = sorted(expiries)

        return expiries

    # --------------------------------------------------
    # Strikes
    # --------------------------------------------------

    def get_strikes(
        self,
        index_name,
        expiry,
    ):

        df = self.load()

        option_df = df[
            (df["name"] == index_name)
            &
            (df["segment"] == "NFO-OPT")
            &
            (df["expiry"] == expiry)
        ]

        strikes = sorted(
            option_df["strike"]
            .unique()
            .tolist()
        )

        return strikes

    # --------------------------------------------------
    # Instrument Token
    # --------------------------------------------------

    def get_token(
        self,
        tradingsymbol,
    ):

        df = self.load()

        row = df[
            df["tradingsymbol"]
            == tradingsymbol
        ]

        if row.empty:
            return None

        return int(
            row.iloc[0]["instrument_token"]
        )

    # --------------------------------------------------
    # Trading Symbol
    # --------------------------------------------------

    def get_tradingsymbol(
        self,
        token,
    ):

        df = self.load()

        row = df[
            df["instrument_token"]
            == token
        ]

        if row.empty:
            return None

        return row.iloc[0]["tradingsymbol"]
    # --------------------------------------------------
    # Spot Instrument
    # --------------------------------------------------

    def get_spot_instrument(self, index_name):

        if index_name not in SPOT_INDICES:
            raise ValueError(f"Unknown Index : {index_name}")

        config = SPOT_INDICES[index_name]

        exchange = config["exchange"]
        symbol = config["tradingsymbol"]

        df = self.load()

        row = df[
            (df["exchange"] == exchange)
            &
            (df["tradingsymbol"] == symbol)
        ]

        if row.empty:
            raise ValueError(
                f"Unable to locate {symbol}"
            )

        return row.iloc[0]


    # --------------------------------------------------
    # Spot Token
    # --------------------------------------------------

    def get_spot_token(self, index_name):

        row = self.get_spot_instrument(index_name)

        return int(row["instrument_token"])


    # --------------------------------------------------
    # Spot Quote Symbol
    # --------------------------------------------------

    def get_spot_quote_symbol(self, index_name):

        row = self.get_spot_instrument(index_name)

        return f'{row["exchange"]}:{row["tradingsymbol"]}'
    
    # --------------------------------------------------
    # Current Weekly Expiry
    # --------------------------------------------------

    def get_current_weekly_expiry(self, index_name):

        expiries = self.get_expiries(index_name)

        return expiries[0]

    # --------------------------------------------------
    # ATM Option
    # --------------------------------------------------

    def get_atm_option(
        self,
        index_name,
        spot_price,
        option_type,
    ):

        expiry = self.get_current_weekly_expiry(index_name)

        strike = round(spot_price / 50) * 50

        df = self.load()

        row = df[
            (df["name"] == index_name)
            &
            (df["segment"] == "NFO-OPT")
            &
            (df["expiry"] == expiry)
            &
            (df["strike"] == strike)
            &
            (df["instrument_type"] == option_type)
        ]

        if row.empty:
            return None

        return row.iloc[0]
