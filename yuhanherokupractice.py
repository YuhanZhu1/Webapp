#This is a prictive for using streamlit, Heroku, and github
import streamlit as st
import pandas as pd
from pandas import Series
from fredapi import Fred
import yfinance as yf
import altair as alt
from PIL import Image 


fred_key = '5b4374b4423e4bc6a2bccd68c4684772'
fred = Fred(api_key=fred_key)
cpi = fred.get_series(series_id='CPIAUCSL')
cpi_df = pd.DataFrame({'Date':cpi.index,'Index':cpi.values}) 

#load sp500 data
sp = yf.Ticker('^GSPC')
sp_df = sp.history(period='max')

#load nasdaq data
nq = yf.Ticker('^IXIC')
nq_df = nq.history(period='max')


st.title("""
This is a prictice of using github, streamlit, and heroku togrther""")

    
st.write("**CPI Raw Data From FRED API**")
cpi_chart = alt.Chart(cpi_df).mark_line().encode(
    x='Date',
    y='Index',
    color=alt.value("#FFAA00"),
    tooltip=['Index','Date']
    ).interactive().properties(
    width=600,
    height=300)

st.write(cpi_chart)
    


st.markdown("""#### Nasdaq Composite""")
st.line_chart(nq_df['Close'])


st.markdown("""#### SP500 Index""")
st.line_chart(sp_df['Close'])
