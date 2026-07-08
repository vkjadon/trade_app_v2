import pandas as pd


class PreviousDay:

    def calculate(self, df):

        df = df.copy()

        # Daily OHLC
        daily = pd.DataFrame({

            "Open": df["Open"].resample("1D").first(),

            "High": df["High"].resample("1D").max(),

            "Low": df["Low"].resample("1D").min(),

            "Close": df["Close"].resample("1D").last(),

        })

        # Previous Day Levels

        daily["PDH"] = daily["High"].shift(1)

        daily["PDL"] = daily["Low"].shift(1)

        daily["PDO"] = daily["Open"].shift(1)

        daily["PDC"] = daily["Close"].shift(1)

        # Merge back

        trade_date = df.index.normalize()

        df["PDH"] = trade_date.map(daily["PDH"])

        df["PDL"] = trade_date.map(daily["PDL"])

        df["PDO"] = trade_date.map(daily["PDO"])

        df["PDC"] = trade_date.map(daily["PDC"])
        
        return df