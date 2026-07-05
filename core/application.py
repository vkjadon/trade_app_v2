from data.market_data_service import MarketDataService
from indicators.indicator_manager import IndicatorManager
from structure.structure_manager import StructureManager


class TradingApplication:

    def __init__(self):

        self.market = MarketDataService()
        self.indicator = IndicatorManager()
        self.structure = StructureManager()

    def run(self, config):

        # ---------------------------------------
        # Load Market Data
        # ---------------------------------------

        df = self.market.get_spot_data(
            symbol=config["symbol"],
            interval=config["interval"],
            trading_date=config["trading_date"],
            lookback_days=config["lookback_days"],
        )

        # ---------------------------------------
        # Indicators
        # ---------------------------------------

        df = self.indicator.calculate(
            df,
            config["settings"],
        )

        # ---------------------------------------
        # Market Structure
        # ---------------------------------------

        df = self.structure.calculate(df)

        # ---------------------------------------
        # Keep Selected Trading Day
        # ---------------------------------------

        df = df[df.index.date == config["trading_date"]]

        return {
            "data": df,
        }