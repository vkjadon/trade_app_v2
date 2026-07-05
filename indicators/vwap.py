def calculate(df):

    df = df.copy()

    typical_price = (

        df["High"]

        +

        df["Low"]

        +

        df["Close"]

    ) / 3

    tpv = typical_price * df["Volume"]

    df["VWAP"] = (

        tpv.cumsum()

        /

        df["Volume"].cumsum()

    )

    return df