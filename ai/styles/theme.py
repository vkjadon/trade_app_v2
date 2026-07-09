import streamlit as st


def apply_theme():

    st.markdown(
        """
<style>

html,
body,
[class*="css"]{
    font-size:14px;
}

.block-container{
    padding-top:1.6rem;
    padding-bottom:0.4rem;
    padding-left:1rem;
    padding-right:1rem;
}

div[data-testid="stMetric"]{
    padding:0.30rem;
}

div[data-testid="stVerticalBlock"]{
    gap:0.30rem;
}

button{
    font-size:14px !important;
}

label{
    font-size:14px !important;
}

div[data-baseweb="select"]{
    font-size:14px;
}

input{
    font-size:14px !important;
}

textarea{
    font-size:14px !important;
}

h1{
    font-size:24px;
    margin-bottom:0.4rem;
}

h2{
    font-size:18px;
    margin-bottom:0.3rem;
}

h3{
    font-size:15px;
    margin-bottom:0.2rem;
}

</style>
""",
        unsafe_allow_html=True,
    )