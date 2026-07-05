import pandas as pd


def calculate(df, period=20):

    df = df.copy()

    df["EMA20"] = (
        df["Close"]
        .ewm(
            span=period,
            adjust=False
        )
        .mean()
    )

    return df