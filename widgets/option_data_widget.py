import streamlit as st


class OptionDataWidget:

    def render(
        self,
        ce,
        pe,
        ce_df,
        pe_df,
    ):

        with st.expander("📈 ATM Option Data", expanded=False):

            st.info(
                f"CE : {ce['tradingsymbol']}    |    PE : {pe['tradingsymbol']}"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.caption("ATM CE")

                st.dataframe(
                    ce_df[
                        [
                            "Open",
                            "High",
                            "Low",
                            "Close",
                            "VWAP",
                            "OI",
                            "Volume",
                            "Volume_SMA20",
                        ]
                    ],
                    use_container_width=True,
                    height=250,
                    hide_index=False,
                )

            with col2:

                st.caption("ATM PE")

                st.dataframe(
                    pe_df[
                        [
                            "Open",
                            "High",
                            "Low",
                            "Close",
                            "VWAP",
                            "OI",
                            "Volume",
                            "Volume_SMA20",
                        ]
                    ],
                    use_container_width=True,
                    height=250,
                    hide_index=False,
                )