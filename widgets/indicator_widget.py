import streamlit as st


class IndicatorWidget:

    def render(self):

        st.sidebar.header("Indicators")

        return {

            "ema": st.sidebar.checkbox(

                "EMA",

                value=True,

            ),

            "rsi": st.sidebar.checkbox(

                "RSI",

                value=True,

            ),

            "macd": st.sidebar.checkbox(

                "MACD",

                value=True,

            ),

            "vwap": st.sidebar.checkbox(

                "VWAP",

                value=False,

            ),

            "volume": st.sidebar.checkbox(

                "Relative Volume",

                value=False,

            ),

        }