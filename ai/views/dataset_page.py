import streamlit as st


def render():

    st.title("📂 Dataset Explorer")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Instruments",
            "3",
        )

    with col2:
        st.metric(
            "Years",
            "-",
        )

    with col3:
        st.metric(
            "Months",
            "-",
        )

    with col4:
        st.metric(
            "Candles",
            "-",
        )

    st.divider()

    st.subheader("Dataset Summary")

    st.info("Dataset summary will appear here.")

    st.divider()

    st.subheader("Missing Data")

    st.warning("No analysis performed.")

    st.divider()

    st.subheader("Storage")

    left, right = st.columns(2)

    with left:
        st.metric(
            "CSV Files",
            "-",
        )

    with right:
        st.metric(
            "Disk Usage",
            "-",
        )