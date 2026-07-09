import streamlit as st

from tasks.task_manager import TaskManager

def render():

    st.title("🤖 AI Market Prediction")
    
    with st.sidebar:
        st.header("Download")
        symbol_dropdown = st.selectbox("Instrument", ["NIFTY", "BANKNIFTY", "SENSEX",],)
        interval_dropdown = st.selectbox("Interval", ["5minute", "15minute", "day",],)
        start_date_picker = st.date_input("Start Date",)
        end_date_picker = st.date_input("End Date",)

        download_master_chekbox = st.checkbox("Download Instrument Master",value=False,)
        download_button = st.button("⬇ Download Historical Data",use_container_width=True,)

    left, right = st.columns([3, 1])

    with left:
        st.subheader("Status")
        st.info("Ready")
        st.progress(0)
        log = st.empty()

    with right:
        st.subheader("Summary")
        st.metric("Files", "0",)
        st.metric("Downloaded", "0",)
        st.metric("Skipped", "0",)

    if download_button:
        log.info("Downloading...")
        manager = TaskManager()
        manager.download(symbols=[symbol_dropdown], interval=interval_dropdown, start_date=start_date_picker, end_date=end_date_picker, download_master=download_master_chekbox,)
        log.success("Completed.")