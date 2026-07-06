from services.market_data_service import MarketDataService


class FuturesDataService:

    def __init__(self):
        self.market = MarketDataService()

    def load(self, config):

        future_config = config.copy()

        future_config["symbol"] = "NIFTYFUT"

        df = self.market.load(future_config)

        return df[["Volume"]].copy()