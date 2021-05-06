import streamlit as st
import numpy as np
import pandas as pd

st.title("🦠TOKYO COVID19 DATA API")
st.write("This is a realtime data visualization of COVID19 in Tokyo. Data source is https://github.com/tokyo-metropolitan-gov/covid19 ")

#load positive rate data
json = pd.read_json("https://raw.githubusercontent.com/tokyo-metropolitan-gov/covid19/development/data/positive_rate.json")
positive_rate = pd.json_normalize(json['data'])
positive_rate['diagnosed_date'] = pd.to_datetime(positive_rate['diagnosed_date'], format='%Y-%m-%d')
st.subheader("- POSITIVE RATE / 陽性率")
st.line_chart(positive_rate[['diagnosed_date', 'positive_rate']].rename(columns={'diagnosed_date':'index'}).set_index('index'))

#positive & negative count
st.subheader("- POSITIVE & NEGATIVE COUNT / 陽性者数・陰性者数")
st.line_chart(positive_rate[['diagnosed_date', 'positive_count', 'negative_count']].rename(columns={'diagnosed_date':'index'}).set_index('index'))

#load deaths data 
json = pd.read_json("https://raw.githubusercontent.com/tokyo-metropolitan-gov/covid19/development/data/deaths.json")
deaths = pd.json_normalize(json['data'])
deaths['death_date'] = pd.to_datetime(deaths['death_date'], format='%Y-%m-%d')
st.subheader("- NUMBER OF DEATHS / 死亡者数")
st.line_chart(deaths[['death_date', 'count']].rename(columns={'death_date':'index'}).set_index('index'))

#hospitalized & severe cases
json = pd.read_json("https://raw.githubusercontent.com/tokyo-metropolitan-gov/covid19/development/data/positive_status.json")
severe = pd.json_normalize(json['data'])
severe['date'] = pd.to_datetime(severe['date'], format='%Y-%m-%d')
st.subheader("- NUMBER OF HOSPITARIZED & SEVERE CASE /")
st.line_chart(severe[['date', 'hospitalized', 'severe_case']].rename(columns={'date':'index'}).set_index('index'))