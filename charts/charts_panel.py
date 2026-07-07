import streamlit as st


class ChartsPanel:

    def render(self, price_chart,
        rsi_chart=None,
        macd_chart=None,
    ):

        st.plotly_chart(
            price_chart,
            use_container_width=True,
        )

        if rsi_chart is not None:

            st.plotly_chart(
                rsi_chart,
                use_container_width=True,
            )

        if macd_chart is not None:

            st.plotly_chart(
                macd_chart,
                use_container_width=True,
            )