import pandas as pd


class Validator:

    REQUIRED_COLUMNS = [
        "Datetime",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
    ]

    def validate(self, df: pd.DataFrame) -> bool:

        if df.empty:
            print("Validation Failed : Empty DataFrame")
            return False

        if not set(self.REQUIRED_COLUMNS).issubset(df.columns):
            print("Validation Failed : Missing Columns")
            return False

        if df["Datetime"].duplicated().any():
            print("Validation Failed : Duplicate Datetime")
            return False

        if not df["Datetime"].is_monotonic_increasing:
            print("Validation Failed : Datetime Not Sorted")
            return False

        if df[self.REQUIRED_COLUMNS].isnull().any().any():
            print("Validation Failed : Null Values")
            return False

        return True