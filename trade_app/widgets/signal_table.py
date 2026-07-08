import streamlit as st


class SignalTable:

    def render(self, df):

        signals = df[["Close", "Signal", "Reason"]].copy()
        signals.insert(0, "Time", signals.index.strftime("%H:%M"))
        
        if signals.empty:
            st.info("No signals generated.")
            return

        st.markdown(f"""<h4 style='margin:0;padding:0;color:#FF4B4B;'>
                    Signals
                    </h4>""", unsafe_allow_html=True,)
        
        st.dataframe(
            signals,
            hide_index=True,
            use_container_width=True,
            column_config={
                "Close": st.column_config.NumberColumn(
                    "Close",
                    width="small",
                    format="%.2f",
                ),
                "Signal": st.column_config.TextColumn(
                    "Signal",
                    width="small",
                ),
                "Reason": st.column_config.TextColumn(
                    "Failed Condition",
                    width="large",
                ),
            },
        )