import streamlit as st

from widgets.sidebar import Sidebar
from widgets.replay_panel import ReplayPanel
from widgets.signal_table import SignalTable
from widgets.trade_book import TradeBook

from charts.candlestick import CandlestickChart
from charts.rsi_chart import RSIChart
from charts.macd_chart import MACDChart
from charts.charts_panel import ChartsPanel

from core.application import TradingApplication
from strategy.trading_strategy import TradingStrategy
from engine.trade_engine import TradeEngine


# --------------------------------------------------------
# Page
# --------------------------------------------------------

st.set_page_config(
    page_title="Om Trade",
    layout="wide",
)

st.title("📈 Trade App V2")


# --------------------------------------------------------
# Sidebar
# --------------------------------------------------------

sidebar = Sidebar()
config = sidebar.render()

settings = config["settings"]


# --------------------------------------------------------
# Load Data
# --------------------------------------------------------

app = TradingApplication()

result = app.run(config)

df = result["data"]


# --------------------------------------------------------
# Replay
# --------------------------------------------------------

step = ReplayPanel().render(len(df))

df = df.iloc[:step].copy()


# --------------------------------------------------------
# Strategy
# --------------------------------------------------------

strategy = TradingStrategy()

df = strategy.generate_signals(
    df,
    settings,
)


# --------------------------------------------------------
# Trades
# --------------------------------------------------------

trade_engine = TradeEngine()

trades = trade_engine.generate(df)


# --------------------------------------------------------
# Charts
# --------------------------------------------------------

price_chart = CandlestickChart().create(
    df,
    trades,
)

rsi_chart = None
macd_chart = None

if settings["rsi"]:
    rsi_chart = RSIChart().create(df)

if settings["macd"]:
    macd_chart = MACDChart().create(df)

ChartsPanel().render(price_chart)
ChartsPanel().render(rsi_chart, macd_chart)


# --------------------------------------------------------
# Trade Book
# --------------------------------------------------------

TradeBook().render(trades)


# --------------------------------------------------------
# Signal Table
# --------------------------------------------------------

st.subheader("Signals")

SignalTable().render(df)