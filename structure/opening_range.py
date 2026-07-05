import pandas as pd


class OpeningRange:

    def __init__(self, minutes=15):

        self.minutes = minutes

    def calculate(self, df):

        df = df.copy()

        # ------------------------------------------
        # Number of candles in Opening Range
        # ------------------------------------------

        interval = self._get_interval_minutes(df)

        candles = max(1, self.minutes // interval)

        # ------------------------------------------

        df["ORH"] = pd.NA
        df["ORL"] = pd.NA
        df["ORM"] = pd.NA
        df["OR_WIDTH"] = pd.NA

        # ------------------------------------------
        # Process each trading day
        # ------------------------------------------

        for _, day_df in df.groupby(df.index.date):

            opening = day_df.iloc[:candles]

            if opening.empty:
                continue

            or_high = opening["High"].max()
            or_low = opening["Low"].min()

            df.loc[day_df.index, "ORH"] = or_high
            df.loc[day_df.index, "ORL"] = or_low
            df.loc[day_df.index, "ORM"] = (or_high + or_low) / 2
            df.loc[day_df.index, "OR_WIDTH"] = or_high - or_low

        return df

    # --------------------------------------------------
    # Detect chart interval automatically
    # --------------------------------------------------

    def _get_interval_minutes(self, df):

        if len(df) < 2:
            return 5

        delta = df.index[1] - df.index[0]

        return int(delta.total_seconds() / 60)