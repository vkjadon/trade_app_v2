import streamlit as st
from streamlit_option_menu import option_menu

from styles.theme import apply_theme

from views.dashboard_view import render as dashboard_view
from views.downloader_view import render as downloader_view
from views.dataset_view import render as dataset_view

# ---------------------------------------------------------
# Streamlit Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Trading",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ---------------------------------------------------------
# Theme
# ---------------------------------------------------------

apply_theme()


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    st.title("🤖 AI Trading")

    st.caption("Market Prediction Platform")

    st.divider()

    page = option_menu(

        menu_title=None,

        options=[
            "Dashboard",
            "Downloader",
            "Dataset",
            "Feature Engineering",
            "Label Generator",
            "Model Training",
            "Prediction",
            "Backtesting",
            "Settings",
            "Logs",
        ],

        icons=[
            "house",
            "cloud-download",
            "database",
            "cpu",
            "bullseye",
            "robot",
            "graph-up-arrow",
            "activity",
            "gear",
            "journal-text",
        ],

        default_index=0,

        styles={
            "container": {
                "padding": "0!important",
                "background-color": "transparent",
            },
            "icon": {
                "font-size": "16px",
            },
            "nav-link": {
                "font-size": "14px",
                "text-align": "left",
                "margin": "2px",
                "border-radius": "6px",
            },
        },
    )

    st.divider()

    st.caption("Project")

    st.metric("Dataset", "--")

    st.metric("CSV Files", "--")

    st.metric("Candles", "--")

    st.metric("Storage", "--")

    st.divider()

    st.success("Ready")


# ---------------------------------------------------------
# Main Area
# ---------------------------------------------------------

if page == "Dashboard":

    dashboard_view()

elif page == "Downloader":

    downloader_view()

elif page == "Dataset":

    dataset_view()

else:

    st.info(f"'{page}' module is under development.")