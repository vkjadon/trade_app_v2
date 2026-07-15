import streamlit as st


def render():

    st.title("📥 Historical Data Downloader")

    st.caption("Download historical market data for AI model training.")

    st.divider()

    # ==========================================================
    # Download Parameters
    # ==========================================================

    c1, c2 = st.columns(2)

    with c1:

        symbol = st.selectbox(
            "Instrument",
            [
                "NIFTY",
                "BANKNIFTY",
                "SENSEX",
            ],
        )

        interval = st.selectbox(
            "Interval",
            [
                "5minute",
                "15minute",
                "day",
            ],
        )

    with c2:

        start_date = st.date_input(
            "Start Date",
        )

        end_date = st.date_input(
            "End Date",
        )

        download_master = st.checkbox(
            "Download Instrument Master",
            value=False,
        )

    st.divider()

    # ==========================================================
    # Actions
    # ==========================================================

    col1, col2, col3 = st.columns([1, 1, 4])

    with col1:

        download = st.button(
            "⬇ Download",
            use_container_width=True,
        )

    with col2:

        st.button(
            "🗑 Clear Logs",
            use_container_width=True,
        )

    st.divider()

    # ==========================================================
    # Progress
    # ==========================================================

    st.subheader("Progress")

    progress = st.progress(0)

    status = st.empty()

    st.divider()

    # ==========================================================
    # Logs
    # ==========================================================

    st.subheader("Download Log")

    log = st.empty()

    # ==========================================================
    # Download
    # ==========================================================

    if download:

        status.info("Starting download...")

        progress.progress(10)

        log.info("Initializing downloader...")

        # ------------------------------------------------------
        # DownloadManager will be called here
        # ------------------------------------------------------

        progress.progress(100)

        status.success("Download completed.")