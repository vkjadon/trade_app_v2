from pathlib import Path

import pandas as pd
from config import MARKET_OPEN, MARKET_CLOSE, CANDLES_PER_DAY

class DatasetBuilder:

    def __init__(self):

        self.candles_per_day = CANDLES_PER_DAY
    # ---------------------------------------------------------

    def prepare(self, csv_file):

        df = pd.read_csv(csv_file)

        df["Datetime"] = pd.to_datetime(df["Datetime"])
        
        df = self._market_hours(df)
        
        df = df.sort_values("Datetime")

        df["TradingDate"] = df["Datetime"].dt.date

        days = {}

        for trading_day, day_df in df.groupby("TradingDate"):

            days[trading_day] = day_df.reset_index(drop=True)

        return days

    # ---------------------------------------------------------

    def validate(self, days):

        print()

        print(f"{'Date':<12} {'Candles':>8}")

        print("-" * 22)

        all_valid = True

        for trading_day, day_df in days.items():

            candles = len(day_df)

            print(f"{trading_day} {candles:>8}")

            if candles != self.candles_per_day:

                all_valid = False

        print("-" * 22)

        print()

        if all_valid:

            print("✅ All trading days have 75 candles.")

        else:

            print("❌ Some trading days do not have 75 candles.")

        return all_valid
    
    def _market_hours(self, df):

      return df[
        df["Datetime"].dt.time.between(
            MARKET_OPEN,
            MARKET_CLOSE,
        )
    ]