import streamlit as st
import time


class ReplayPanel:

    def render(self, total_candles, trading_date):

# Reset replay when trading date changes
        if (
            "replay_date" not in st.session_state
            or st.session_state.replay_date != trading_date
        ):
            st.session_state.replay_date = trading_date
            st.session_state.step = total_candles
    
        # ---------------------------------------
        # No data available
        # ---------------------------------------

        if total_candles == 0:
            st.sidebar.subheader("▶ Replay")
            st.sidebar.info("No market data available.")
            return 0

        # ---------------------------------------
        # Initialize
        # ---------------------------------------

        if (
            "step" not in st.session_state
            or st.session_state.step < 1
            or st.session_state.step > total_candles
        ):
            st.session_state.step = total_candles

        if "playing" not in st.session_state:
            st.session_state.playing = False

        # ---------------------------------------
        # Replay
        # ---------------------------------------

        st.sidebar.subheader("▶ Replay")

        c1, c2 = st.sidebar.columns(2)

        if c1.button("⏮ Prev", use_container_width=True):
            st.session_state.step = max(
                1,
                st.session_state.step - 1,
            )

        if c2.button("Next ⏭", use_container_width=True):
            st.session_state.step = min(
                total_candles,
                st.session_state.step + 1,
            )

        c1, c2 = st.sidebar.columns(2)

        if c1.button("▶ Replay", use_container_width=True):
            st.session_state.playing = True

        if c2.button("⏸ Pause", use_container_width=True):
            st.session_state.playing = False

        # ---------------------------------------
        # Slider
        # ---------------------------------------

        # No replay possible
        if total_candles <= 1:

            st.sidebar.info(f"Candles : {total_candles}")

            return total_candles

        step = st.sidebar.slider(
            "Candle",
            min_value=1,
            max_value=total_candles,
            value=st.session_state.step,
        )

        st.session_state.step = step

        st.sidebar.caption(
            f"Candle : {step}/{total_candles}"
        )

        # ---------------------------------------
        # Auto Replay
        # ---------------------------------------

        if st.session_state.playing:

            if step < total_candles:

                time.sleep(0.4)

                st.session_state.step += 1

                st.rerun()

            else:

                st.session_state.playing = False

        return st.session_state.step