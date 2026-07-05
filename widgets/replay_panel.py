import streamlit as st


class ReplayPanel:

    def render(self, total_candles):

        if "step" not in st.session_state:
            st.session_state.step = min(30, total_candles)

        if "playing" not in st.session_state:
            st.session_state.playing = False

        st.sidebar.subheader("▶ Replay")

        c1, c2 = st.sidebar.columns(2)

        if c1.button("⏮ Prev", use_container_width=True):
            st.session_state.step = max(1, st.session_state.step - 1)

        if c2.button("Next ⏭", use_container_width=True):
            st.session_state.step = min(total_candles,
                                        st.session_state.step + 1)

        c1, c2 = st.sidebar.columns(2)

        if c1.button("▶ Replay", use_container_width=True):
            st.session_state.playing = True

        if c2.button("⏸ Pause", use_container_width=True):
            st.session_state.playing = False

        st.sidebar.slider(
            "Candle",
            1,
            total_candles,
            key="step",
        )

        st.sidebar.write(
            f"**Candle:** {st.session_state.step}/{total_candles}"
        )

        return st.session_state.step