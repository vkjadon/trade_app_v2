import pandas as pd
import streamlit as st


class TradeBook:

    def render(self, trades):

        st.subheader("📒 Trade Book")

        if not trades:

            st.info("No trades generated.")

            return

        rows = []

        running_pl = 0.0

        for trade in trades:

            running_pl += trade.points

            rows.append({

                "Signal": trade.signal,

                "Entry Time": trade.entry_time.strftime("%H:%M"),

                "Exit Time": trade.exit_time.strftime("%H:%M"),

                "Entry": round(trade.entry_price, 2),

                "Exit": round(trade.exit_price, 2),

                "Points": round(trade.points, 2),

                "Running P/L": round(running_pl, 2),

                "Score": trade.score,

                "Confidence": trade.confidence,

                "Status": trade.status,

                "Exit Reason": trade.exit_reason,

                "Reason": "\n".join(trade.reason),

            })

        df = pd.DataFrame(rows)

        st.dataframe(

            df,

            use_container_width=True,

            hide_index=True,

            height=500,

        )