#This is a prictive for using streamlit, Heroku, and github
import streamlit as st
import altair as alt
from vega_datasets import data

import numpy as np
import pandas as pd
import seaborn as sns

unemp = data.unemployment_across_industries()

unemp["yyyy/mm"] = unemp["year"].astype(str) + '.' + unemp["month"].astype(str)
unemp['yyyy/mm'] = unemp['yyyy/mm'].astype('float')

st.title("""
This is a prictice of using github, streamlit, and heroku togrther

**Check the sidebar for more detail**
""")
print(unemp.head())

first = st.sidebar.button("Count VS Rate")
if first:
    st.write("Count and Rate: with tooltip")
    fig1 = alt.Chart(unemp).mark_point().encode(
    x ='count',
    y ='rate',
    color ='series',
    
    tooltip=['series', 'rate', 'count', 'date']).interactive()

    fig1

second = st.sidebar.button("Histgram")

if second:
    st.write("Date and mean count")
    fig2 = alt.Chart(unemp).mark_bar().encode(
    x ='yyyy/mm',
    y ='mean(count)',
    color ='series').interactive()

    fig2
