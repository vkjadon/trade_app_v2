import streamlit as st

from styles.theme import compact_card, market_snapshot, option_snapshot

from widgets.strategy_widget import StrategyWidget
from widgets.market_widget import MarketWidget
from widgets.option_data_widget import OptionDataWidget

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

from backtest.backtest_engine import BacktestEngine

# --------------------------------------------------------
# Page
# --------------------------------------------------------

st.set_page_config(
    page_title="Om Trade",
    layout="wide",
)

# --------------------------------------------------------
# Sidebar
# --------------------------------------------------------

market = MarketWidget().render()

settings = StrategyWidget().render()

backtest = st.sidebar.button("📊 Backtest",use_container_width=True,)

config = {
    **market,
    "settings": settings,
}

st.markdown(
    f"""
    <h4 style='margin:0;padding:0;color:#FF4B4B;'>
        {config["symbol"]} | {config["trading_date"]:%d-%b-%Y} | {config["interval"]}
    </h4>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------
# Load Data
# --------------------------------------------------------

app = TradingApplication()

result = app.run(config)

if result is None:
    st.info("No market data available for the selected date.")
    st.stop()
    
df = result["data"]

# --------------------------------------------------------
# Backtest
# --------------------------------------------------------

if settings["strategy"] == "Smart ORB":

    OptionDataWidget().render(
        result["ce"],
        result["pe"],
        result["ce_df"],
        result["pe_df"],
    )
    
if backtest:

    st.subheader("📊 Backtest")

    bt = BacktestEngine().run(config)

    if bt.empty:

        st.warning("No trades generated.")

    else:

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Days", len(bt))
        c2.metric("Trades", bt["Trades"].sum())
        c3.metric("Points", round(bt["Points"].sum(), 2))
        c4.metric("Win %", round(100 * bt["Wins"].sum() /
                                 max(1, bt["Trades"].sum()), 1))

        st.dataframe(
            bt,
            use_container_width=True,
            hide_index=True,
        )

        st.line_chart(
            bt.set_index("Date")["Cum Points"]
        )

    st.stop()
    
# --------------------------------------------------------
# Replay
# --------------------------------------------------------

# st.write("Rows before replay:", len(df))

step = ReplayPanel().render(len(df), config["trading_date"])

# st.write("Step:", step)

df = df.iloc[:step].copy()

# st.write("Rows after replay:", len(df))

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

price_chart = CandlestickChart().create(df,trades,)

rsi_chart = None
macd_chart = None

rsi_chart = RSIChart().create(df)
macd_chart = MACDChart().create(df)
    
left, right = st.columns([3, 1], gap="small")

with left:
    ChartsPanel().render(price_chart)
    TradeBook().render(trades)
    
with right:

    st.write("Market Snapshot")
    last = df.iloc[-1]
    market_snapshot(last)

    if result["ce_df"] is not None:

        # ce = result["ce_df"].iloc[-1]
        # pe = result["pe_df"].iloc[-1]

        current_time = df.index[-1]
        # ce = ce_df.loc[current_time]
        # pe = pe_df.loc[current_time]
        ce = result["ce_df"].loc[current_time]
        pe = result["pe_df"].loc[current_time]

        option_snapshot(ce, pe)
            
    ChartsPanel().render(rsi_chart, macd_chart)

SignalTable().render(df)

