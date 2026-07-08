from trade_app.data.instrument_manager import InstrumentManager

def test_option_metadata():

    im = InstrumentManager()

    df = im.load()

    print("\n----- NIFTYIT -----")
    print(
        df[
            df["tradingsymbol"].str.contains("NIFTYIT", case=False, na=False)
        ][["name", "tradingsymbol", "segment", "exchange"]].drop_duplicates()
    )

    print("\n----- SENSEX -----")
    print(
        df[
            df["tradingsymbol"].str.contains("SENSEX", case=False, na=False)
        ][["name", "tradingsymbol", "segment", "exchange"]].drop_duplicates()
    )