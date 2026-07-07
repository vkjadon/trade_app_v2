import streamlit as st
from datetime import date, timedelta


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

        symbol = st.sidebar.selectbox("",["NIFTY","BANKNIFTY","NIFTYIT","SENSEX",],label_visibility="collapsed", )

        # -----------------------------
        # Trading Date
        # -----------------------------
        c1, c2 = st.sidebar.columns([2, 1])

        trading_date = c1.date_input("", value=today,max_value=today,label_visibility="collapsed",)

        interval = c2.selectbox("",["5minute","15minute",],label_visibility="collapsed",)
        
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