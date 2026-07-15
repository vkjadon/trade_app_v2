import streamlit as st
import pandas as pd

from dataset.dataset_manager import DatasetManager


def render_sidebar():

    st.title("📂 Dataset")

    st.button(
        "🔄 Refresh",
        use_container_width=True,
    )

    st.checkbox(
        "Show Missing Months",
        value=True,
    )

    st.checkbox(
        "Show Corrupt Files",
        value=True,
    )


def render():

    manager = DatasetManager()

    data = manager.summary()

    summary = data["summary"]

    st.title("📂 Dataset Explorer")

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric("Instruments", summary["instruments"])
    c2.metric("Years", summary["years"])
    c3.metric("Months", summary["months"])
    c4.metric("Files", summary["files"])
    c5.metric("Candles", f"{summary['candles']:,}")

    st.divider()

    left, right = st.columns([3, 1])

    with left:

        st.subheader("Dataset")

        records = pd.DataFrame(data["records"])

        if records.empty:

            st.info("No dataset found.")

        else:

            st.dataframe(
                records,
                use_container_width=True,
                hide_index=True,
                height=400,
            )

    with right:

        st.subheader("Storage")

        st.metric("CSV Files", summary["files"])

        st.metric(
            "Disk Usage",
            f"{summary['size_mb']:.2f} MB",
        )

        st.metric(
            "Last Download",
            "-",
        )