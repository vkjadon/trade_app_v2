from widgets.market_widget import MarketWidget
from widgets.strategy_widget import StrategyWidget


class Sidebar:

    def render(self):

        market = MarketWidget().render()

        strategy = StrategyWidget().render()

        return {

            **market,

            "settings": strategy,

        }