import streamlit as st

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
)

def load_css():

    st.markdown("""
    <style>

    /* ---------- Main ---------- */

    .block-container{
        padding-top:0rem;
        padding-bottom:0rem;
        padding-left:0.5rem;
        padding-right:0.5rem;
    }

    /* ---------- Headings ---------- */

    h1,h2,h3,h4{
        margin:0 !important;
        padding:0;
    }

    /* ---------- Metrics ---------- */

    .stMetric{
        border-radius:6px;
        border:1px solid #DDD;
        padding:6px;
    }

    div[data-testid="stVerticalBlock"]{
        gap:0.2rem;
    }

    /* ---------- DataFrame ---------- */

    div[data-testid="stDataFrame"]{
        font-size:11px;
    }

    div[data-testid="stDataEditor"]{
        font-size:11px;
    }

    table{
        font-size:10px !important;
        line-height:1.0 !important;
    }

    th{
        padding:2px 2px !important;
    }

    td{
        padding:2px 2px !important;
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
        margin:0.05rem 0;
    }

    </style>
    """, unsafe_allow_html=True)

def compact_card(
    title,
    value,
    color="#FFFFFF",
    background="#202124",
    border="#3A3A3A",
):

    st.html(f"""
    <div style="
        background:{background};
        border:1px solid {border};
        border-radius:8px;
        padding:8px;
        margin-bottom:6px;
    ">
        <div style="
            font-size:11px;
            color:#A0A0A0;
        ">
            {title}
        </div>

        <div style="
            font-size:16px;
            font-weight:bold;
            color:{color};
        ">
            {value}
        </div>
    </div>
    """)

def market_snapshot(last):

    st.html(f"""
    <div style="
        border:1px solid #3A3A3A;
        border-radius:10px;
        padding:0px;
        margin-bottom:2px;
    ">

        <table style="width:100%; font-size:12px;">

            <tr>
                <td style="color:#A0A0A0;">Close</td>
                <td align="right"><b>{last['Close']:.2f}</b></td>
            </tr>

            <tr>
                <td style="color:#A0A0A0;">EMA20</td>
                <td align="right"><b>{last['EMA20']:.2f}</b></td>
            </tr>

            <tr>
                <td style="color:#A0A0A0;">RSI</td>
                <td align="right"><b>{last['RSI']:.1f}</b></td>
            </tr>

            <tr>
                <td style="color:#A0A0A0;">MACD</td>
                <td align="right"><b>{last['MACD']:.2f}</b></td>
            </tr>

            <tr>
                <td style="color:#A0A0A0;">Signal</td>
                <td align="right"><b>{last['Signal']}</b></td>
            </tr>

            
        </table>

    </div>
    """)
    
def option_snapshot(ce, pe):

    st.html(f"""
    <div style="
        border:1px solid #3A3A3A;
        border-radius:10px;
        padding:0px;
        margin-bottom:2px;
    ">

        <table style="width:100%; font-size:12px;">

            <tr>
                <td style="color:#A0A0A0;"></td>
                <td align="right" style="color:#A0A0A0;">CE</td>
                <td align="right" style="color:#A0A0A0;">PE</td>
            </tr>
            <tr>
                <td style="color:#A0A0A0;">Close</td>
                <td align="right"><b>{ce["Close"]:.2f}</b></td>
                <td align="right"><b>{pe["Close"]:.2f}</b></td>
            </tr>

            <tr>
                <td style="color:#A0A0A0;">VWAP</td>
                <td align="right"><b>{ce['VWAP']:.2f}</b></td>
                <td align="right"><b>{pe['VWAP']:.2f}</b></td>
            </tr>

            <tr>
                <td style="color:#A0A0A0;">Volume</td>
                <td align="right"><b>{ce['Volume']/1000:.2f}k</b></td>
                <td align="right"><b>{(pe['Volume']/1000):.2f}k</b></td>
            </tr>

            <tr>
                <td style="color:#A0A0A0;">OI</td>
                <td align="right"><b>{(ce['OI']/100000):0.2f} l</b></td>
                <td align="right"><b>{(pe['OI']/100000):0.2f} l</b></td>
            </tr>
        </table>

    </div>
    """)