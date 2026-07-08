import streamlit as st


class TradeBook:

    def render(self, trades):

        st.write("Trade Book")

        if trades.empty:
            st.info("No trades generated.")
            return

        trades = trades.copy()

        trades["Entry Time"] = trades["Entry Time"].dt.strftime("%H:%M")
        trades["Exit Time"] = trades["Exit Time"].dt.strftime("%H:%M")

        trades["Entry"] = trades["Entry"].round(2)
        trades["Exit"] = trades["Exit"].round(2)
        trades["Points"] = trades["Points"].round(2)

        trades["Running P/L"] = trades["Points"].cumsum().round(2)

        trades = trades.reset_index(drop=True)

        st.dataframe(
            trades[["Entry Time", "Entry", "SL", "Target", "Exit", "Exit Time", "Points", "Running P/L"]],
            use_container_width=True,
            hide_index=True,
        )