import streamlit as st


def render():

    st.title("🏠 Dashboard")

    st.info("Welcome to AI Trading Platform")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Dataset", "Ready")
    c2.metric("Features", "Pending")
    c3.metric("Model", "Not Trained")
    c4.metric("Prediction", "Idle")

    st.divider()

    st.subheader("Project Status")

    st.write("This dashboard will display the overall status of the AI pipeline.")