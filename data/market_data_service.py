from data.market_data import MarketData


class MarketDataService:

    def __init__(self):

        self.market = MarketData()

    # --------------------------------------------------
    # Spot Data
    # --------------------------------------------------

    def get_spot_data(
        self,
        symbol,
        interval="5minute",
        trading_date=None,
        lookback_days=10,
    ):

        return self.market.get_spot_data(
            index_name=symbol,
            interval=interval,
            trading_date=trading_date,
            lookback_days=lookback_days,
        )

    # --------------------------------------------------
    # Option Data (Instrument Token)
    # --------------------------------------------------

    def get_option_data_by_token(
        self,
        instrument_token,
        interval="5minute",
        trading_date=None,
        lookback_days=10,
    ):

        return self.market.get_history_by_token(
            instrument_token=instrument_token,
            interval=interval,
            trading_date=trading_date,
            lookback_days=lookback_days,
        )

    # --------------------------------------------------
    # LTP
    # --------------------------------------------------

    def get_ltp(
        self,
        symbol,
    ):

        return self.market.get_ltp(symbol)

    # --------------------------------------------------
    # Quote
    # --------------------------------------------------

    def get_quote(
        self,
        symbol,
    ):

        return self.market.get_quote(symbol)
    
    