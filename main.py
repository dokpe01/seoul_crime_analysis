import streamlit as st
import os
import altair as alt
import pandas as pd

st.markdown("""
    <style>
    .stVerticalBlock {
        justify-content: center;
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def page_config():
    st.set_page_config(
        page_title="Seoul Crime Analysis",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="auto")
    alt.themes.enable("dark")

def main():
    page_config()
    st.title("TEST")

if __name__ == "__main__":
    main()