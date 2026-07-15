import streamlit as st

from styles.colors import (
    PRIMARY,
    TEXT,
    WHITE,
    BORDER,
)


def apply_theme():

    st.markdown(
        f"""
<style>

/* ---------- Global ---------- */

html,
body,
[class*="css"]{{
    font-size:14px;
}}

/* ---------- Main Container ---------- */

.block-container{{
    padding-top:2.50rem;
    padding-bottom:0.30rem;
    padding-left:0.80rem;
    padding-right:0.80rem;
}}

/* ---------- Vertical Spacing ---------- */

div[data-testid="stVerticalBlock"]{{
    gap:1.15rem;
}}

/* ---------- Sidebar ---------- */

section[data-testid="stSidebar"]{{
    padding-top:0.30rem;
}}

/* ---------- Buttons ---------- */

.stButton > button{{
    font-size:14px !important;
    padding:0.25rem 0.80rem !important;
    border-radius:6px;
}}

/* ---------- Labels ---------- */

div[data-testid="stWidgetLabel"]{{
    font-size:14px !important;
    font-weight:500;
}}

/* ---------- Select ---------- */

div[data-baseweb="select"]{{
    font-size:14px !important;
}}

/* ---------- Inputs ---------- */

.stTextInput input,
.stNumberInput input,
.stDateInput input,
textarea{{
    font-size:14px !important;
}}

/* ---------- Metrics ---------- */

div[data-testid="stMetric"]{{
    padding:0.20rem !important;
    border-radius:6px;
}}

/* ---------- Headers ---------- */

h1{{
    font-size:24px !important;
    margin-bottom:0.40rem;
}}

h2{{
    font-size:18px !important;
    margin-bottom:0.30rem;
}}

h3{{
    font-size:15px !important;
    margin-bottom:0.20rem;
}}

/* ---------- Tabs ---------- */

button[data-baseweb="tab"]{{
    font-size:14px !important;
    font-weight:600 !important;
    color:{TEXT} !important;
    background:transparent !important;
    padding:0.35rem 0.90rem !important;
}}

button[data-baseweb="tab"]:hover{{
    color:{WHITE} !important;
}}

button[data-baseweb="tab"][aria-selected="true"]{{
    color:{PRIMARY} !important;
    border-bottom:2px solid {PRIMARY} !important;
}}

/* ---------- Divider ---------- */

hr{{
    margin-top:0.40rem;
    margin-bottom:0.40rem;
    border-color:{BORDER};
}}

</style>
""",
        unsafe_allow_html=True,
    )