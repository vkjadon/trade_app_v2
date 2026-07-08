import streamlit as st
from datetime import date, timedelta
from config.symbols import SPOT_INDICES


class MarketWidget:

    def render(self):

        today = date.today()

        if today.weekday() == 5:
            today -= timedelta(days=1)
        elif today.weekday() == 6:
            today -= timedelta(days=2)

        # -----------------------------
        # Symbol & Interval
        # -----------------------------
        
        symbols = list(SPOT_INDICES.keys())

        symbol = st.sidebar.selectbox( "", options=symbols,label_visibility="collapsed",)

        # -----------------------------
        # Trading Date
        # -----------------------------
        c1, c2 = st.sidebar.columns([1, 1])

        trading_date = c1.date_input("", value=today,max_value=today,label_visibility="collapsed",)

        interval = c2.selectbox("",["15minute", "5minute",],label_visibility="collapsed",)
        
        # -----------------------------
        # Lookback
        # -----------------------------

        lookback = st.sidebar.slider(
            "Lookback",
            min_value=5,
            max_value=60,
            value=10,
        )

        return {
            "symbol": symbol,
            "interval": interval,
            "trading_date": trading_date,
            "lookback_days": lookback,
        }