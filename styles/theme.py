import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        .block-container{

            padding-top:1rem;

            padding-bottom:1rem;

        }

        .stMetric{

            border-radius:10px;

            padding:10px;

            border:1px solid #DDD;

        }

        </style>
        """,
        unsafe_allow_html=True,
    )