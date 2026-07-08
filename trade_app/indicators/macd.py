def calculate(df):

    df = df.copy()

    ema12 = df["Close"].ewm(
        span=12,
        adjust=False
    ).mean()

    ema26 = df["Close"].ewm(
        span=26,
        adjust=False
    ).mean()

    df["MACD_12_26_9"] = ema12 - ema26

    df["MACDs_12_26_9"] = (
        df["MACD_12_26_9"]
        .ewm(
            span=9,
            adjust=False
        )
        .mean()
    )

    df["MACDh_12_26_9"] = (
        df["MACD_12_26_9"]
        -
        df["MACDs_12_26_9"]
    )

    # Standard column names used by strategy

    df["MACD"] = df["MACD_12_26_9"]

    df["MACDSignal"] = df["MACDs_12_26_9"]

    df["MACDHistogram"] = df["MACDh_12_26_9"]
    
    return df