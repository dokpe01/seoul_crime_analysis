import streamlit as st
import os
import altair as alt
import pandas as pd
from app.region_app import run_region_app

st.markdown("""
    <style>
    .stVerticalBlock {
        justify-content: center;
        align-items: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.set_page_config(
    page_title="Seoul Crime Analysis",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="auto")
alt.themes.enable("dark")

def main():
    st.title("TEST")
    
    tab_region, tab_time = st.tabs(["자치구별 생활인구", "시간대별"])

    with tab_region:
        run_region_app()

    with tab_time:
        pass

if __name__ == "__main__":
    main()