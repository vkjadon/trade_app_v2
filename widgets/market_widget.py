import streamlit as st

from datetime import date, timedelta


class MarketWidget:

    def render(self):

        st.sidebar.header("Market")

        symbol = st.sidebar.selectbox(

            "Index",

            [

                "NIFTY",

                "BANKNIFTY",

                "FINNIFTY",

                "MIDCPNIFTY",

            ],

        )

        today = date.today()

        if today.weekday() == 5:

            today -= timedelta(days=1)

        elif today.weekday() == 6:

            today -= timedelta(days=2)

        trading_date = st.sidebar.date_input(

            "Trading Date",

            value=today,

            max_value=today,

        )

        interval = st.sidebar.selectbox(

            "Interval",

            [

                "5minute",

                "15minute",

            ],

        )

        lookback = st.sidebar.slider(

            "Lookback Days",

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