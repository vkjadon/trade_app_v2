from data.instrument_manager import InstrumentManager
from data.market_data import MarketData
import datetime

def test_get_atm_option():

    im = InstrumentManager()
    market_data = MarketData()

    option = im.get_atm_option(
        "NIFTY",
        25243,
        "CE",
    )

    assert option is not None
    assert option["instrument_type"] == "CE"
    assert option["strike"] == 25250

    print(option["tradingsymbol"])
    
    option = im.get_atm_option(
        "NIFTY",
        25243,
        "CE",
    )

    df = market_data.get_option_data_by_token(
        option["instrument_token"],
        interval="5minute",
        trading_date=datetime.date(2026, 7, 3),
        lookback_days=5,
    )

    print(df.head())