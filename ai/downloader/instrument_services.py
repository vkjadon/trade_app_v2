from pathlib import Path

import pandas as pd

from config import SPOT_INDICES


class InstrumentService:

    def __init__(self, kite):

        self.kite = kite

        self.instrument_file = (
            Path(__file__).resolve().parents[1]
            / "data"
            / "instruments"
            / "instruments.csv"
        )

        self._df = None

    def load(self):

        print(f"Instrument File : {self.instrument_file}")
        print(f"Exists          : {self.instrument_file.exists()}")

        if self._df is None:

            if not self.instrument_file.exists():

                self.instrument_file.parent.mkdir(
                    parents=True,
                    exist_ok=True,
                )

                self._download_instruments()

            self._df = pd.read_csv(
                self.instrument_file,
                parse_dates=["expiry"],
            )

        return self._df

    def _download_instruments(self):

        print("Downloading instrument master...")

        instruments = self.kite.instruments()

        df = pd.DataFrame(instruments)

        df.to_csv(
            self.instrument_file,
            index=False,
        )

        print(f"Saved : {self.instrument_file}")

    def get_spot_token(
        self,
        symbol,
    ):

        df = self.load()

        row = df[
            (df["exchange"] == SPOT_INDICES[symbol]["exchange"])
            &
            (df["tradingsymbol"] == SPOT_INDICES[symbol]["tradingsymbol"])
        ]

        if row.empty:
            raise ValueError(f"Spot instrument not found: {symbol}")

        return int(row.iloc[0]["instrument_token"])

    def get_spot_info(
        self,
        symbol,
    ):

        df = self.load()

        row = df[
            (df["exchange"] == SPOT_INDICES[symbol]["exchange"])
            &
            (df["tradingsymbol"] == SPOT_INDICES[symbol]["tradingsymbol"])
        ]

        if row.empty:
            raise ValueError(f"Spot instrument not found: {symbol}")

        return row.iloc[0]
    
    def refresh(self):

        self._download_instruments()

        self._df = None