import streamlit as st
from styles.theme import apply_theme
from pages.downloader_page import render

st.set_page_config(page_title="AI Trading", page_icon="🤖",layout="wide",)

apply_theme()

render()