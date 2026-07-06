import streamlit as st


class StrategyWidget:

    def render(self):

        strategy = st.sidebar.selectbox(
            "Strategy",
            [
                "Classic ORB",
                "Smart ORB",
            ],
        )

        return {
            "strategy": strategy,
        }