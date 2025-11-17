import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static
import altair as alt
import scipy.stats as stats
import json

def style_function(feature):
    return {
        'opacity': 0.7,
        'weight': 1,
        'color': 'white',
        'fillOpacity': 0.2,
        'dashArray': '5, 5',
    }

@st.cache_data
def get_area():
    area = pd.read_csv("./data/자치구별_토지면적.csv")
    return area

@st.cache_data
def get_region():
    region = pd.read_csv("./data/생활인구.csv")
    return region

@st.cache_data
def get_pearson():
    pass

@st.cache_data
def region_map():
    pass

def run_region_app():
    st.header("자치구별 인구밀집도")

    row_region = st.columns(1)
    row_year = st.columns(1)
    row_map, row_pearson = st.columns([5,5])

    with row_map.container(height=500, border=True):

        region = get_region()
        area = get_area()

        region = region.set_index("구")

        ko = folium.Map(
            location=[37.5651, 126.98955], 
            zoom_start=11,
            tiles='cartodbpositron'
            )
        
        geo_path = './data/seoul_municipalities_geo_simple.json'
        geo_str = json.load(open(geo_path, encoding='utf-8'))

        folium.GeoJson(
            geo_str,
            style_function=style_function
        ).add_to(ko)

        kmap = folium.Choropleth(
            geo_data=geo_str,
            data=region,
            columns=[region.index, "2024년"],
            fill_color='YlGnBu',
            fill_opacity=0.7,
            line_opacity=0.2,
            key_on='properties.name',
            legend_name="2024년 생활인구수"
        ).add_to(ko)

        # 툴팁처리 추가
        kmap.geojson.zoom_on_click = False
        kmap.geojson.add_child(
            folium.features.GeoJsonTooltip(['name'],labels=False) # Tooltip
        )


        folium_static(ko)

    with row_pearson.container(height=500, border=True):
        st.header("FUCK YOU")