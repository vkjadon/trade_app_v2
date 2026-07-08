def calculate(df, period=20):

    df = df.copy()

    df["AvgVolume"] = (

        df["Volume"]

        .rolling(period)

        .mean()

    )

    df["RelVolume"] = (

        df["Volume"]

        /

        df["AvgVolume"]

    )

    return df