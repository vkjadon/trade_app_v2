import streamlit as st

from widgets.sidebar import Sidebar

from core.application import TradingApplication

from charts.candlestick import CandlestickChart
from charts.rsi_chart import RSIChart
from charts.macd_chart import MACDChart
from charts.charts_panel import ChartsPanel

from widgets.trade_book import TradeBook

# --------------------------------------------------------
# Page
# --------------------------------------------------------

st.set_page_config(
    page_title="Om Trade",
    layout="wide",
)

st.title("📈 Trade App V2")

sidebar = Sidebar()

config = sidebar.render()

symbol = config["symbol"]

interval = config["interval"]

trading_date = config["trading_date"]

lookback_days = config["lookback_days"]

settings = config["settings"]

# --------------------------------------------------------
# Load
# --------------------------------------------------------

app = TradingApplication()

with st.spinner("Loading Market Data..."):

    result = app.run(config)

df = result["data"]

trades = result["trades"]

# --------------------------------------------------------
# Charts
# --------------------------------------------------------

price_chart = CandlestickChart().create(df)

rsi_chart = None
macd_chart = None

if settings["rsi"]:

    rsi_chart = RSIChart().create(df)

if settings["macd"]:

    macd_chart = MACDChart().create(df)

ChartsPanel().render(price_chart, rsi_chart, macd_chart,)

# --------------------------------------------------------
# Trade Book
# --------------------------------------------------------

TradeBook().render(trades)

# --------------------------------------------------------
# Signals
# --------------------------------------------------------

st.subheader("Signals")

# signals = df[df["Signal"] != "WAIT"]

st.dataframe(
    df[["Close", "Signal", "Reason"]],
    use_container_width=True,
)
