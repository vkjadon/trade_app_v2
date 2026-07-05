from widgets.market_widget import MarketWidget
from widgets.indicator_widget import IndicatorWidget


class Sidebar:

    def render(self):

        market = MarketWidget().render()

        indicators = IndicatorWidget().render()

        return {

            **market,

            "settings": indicators,

        }