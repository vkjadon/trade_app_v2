import streamlit as st


def load_css():

    st.markdown("""
    <style>

    /* ---------- Main ---------- */

    .block-container{
        padding-top:0.35rem;
        padding-bottom:0.35rem;
        padding-left:0.75rem;
        padding-right:0.75rem;
    }

    /* ---------- Headings ---------- */

    h1,h2,h3,h4{
        margin-top:0.15rem !important;
        margin-bottom:0.15rem !important;
        padding:0;
    }

    /* ---------- Metrics ---------- */

    .stMetric{
        border-radius:6px;
        border:1px solid #DDD;
        padding:6px;
    }

    /* ---------- DataFrame ---------- */

    div[data-testid="stDataFrame"]{
        font-size:11px;
    }

    div[data-testid="stDataEditor"]{
        font-size:11px;
    }

    table{
        font-size:11px !important;
        line-height:1.1 !important;
    }

    th{
        padding:4px 6px !important;
    }

    td{
        padding:3px 6px !important;
    }

    /* ---------- Buttons ---------- */

    .stButton button{
        padding:0.2rem 0.6rem;
        font-size:12px;
    }

    /* ---------- Sidebar ---------- */

    section[data-testid="stSidebar"]{
        width:260px;
    }

    hr{
        margin:0.25rem 0;
    }

    </style>
    """, unsafe_allow_html=True)