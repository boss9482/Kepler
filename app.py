import streamlit as st
import pandas as pd
from streamlit_keplergl import keplergl_static
from keplergl import KeplerGl

st.header('This is an app that visualizes Airbnb data in Antwerp!')
st.subheader('A quick tutorial on how to use Streamlit')

df = pd.read_csv("http://data.insideairbnb.com/belgium/vlg/antwerp/2022-09-22/visualisations/listings.csv")

map = KeplerGl(height=400)
map.add_data(df, name='Antwerpen Airbnb data')
keplergl_static(map)
