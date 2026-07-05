import numpy as np


class Swing:

    def __init__(self, lookback=2):

        self.lookback = lookback

    def calculate(self, df):

        df = df.copy()

        df["SwingHigh"] = False
        df["SwingLow"] = False

        highs = df["High"].values
        lows = df["Low"].values

        n = len(df)

        for i in range(self.lookback, n - self.lookback):

            high = highs[i]

            if high == max(
                highs[
                    i-self.lookback :
                    i+self.lookback+1
                ]
            ):

                df.iloc[
                    i,
                    df.columns.get_loc("SwingHigh")
                ] = True

            low = lows[i]

            if low == min(
                lows[
                    i-self.lookback :
                    i+self.lookback+1
                ]
            ):

                df.iloc[
                    i,
                    df.columns.get_loc("SwingLow")
                ] = True

        return df