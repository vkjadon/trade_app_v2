from calendar import monthrange
from datetime import datetime

import pandas as pd

class HistoricalDownloader:

    def __init__(self, kite):
        self.kite = kite

    def download_range(self, instrument_token, interval, from_date, to_date,):

        candles = self.kite.historical_data(instrument_token=instrument_token,
            from_date=from_date, to_date=to_date, interval=interval, oi=False,)

        if not candles:
            return pd.DataFrame()

        df = pd.DataFrame(candles)

        df.rename(
            columns={
                "date": "Datetime",
                "open": "Open",
                "high": "High",
                "low": "Low",
                "close": "Close",
                "volume": "Volume",
            },
            inplace=True,
        )

        return df

    def download_month(self, instrument_token, interval, year, month,):

        from_date = datetime(year, month, 1, 9, 15)
        last_day = monthrange(year, month)[1]
        to_date = datetime(year, month, last_day, 15, 30,)

        return self.download_range(instrument_token, interval, from_date,
            to_date,)