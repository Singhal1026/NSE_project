
import streamlit as st
import pandas as pd
import api

st.title("NSE Stock PRICE")


# url = 'https://archives.nseindia.com/content/equities/EQUITY_L.csv'

url = "C:\\Users\\Hello\\OneDrive\\Desktop\\project1\\combine_data.csv"

equility_data = pd.read_csv(url)

user_input = st.selectbox("ENTRE SYMBOL", equility_data.symbol)

ans = api.get(user_input)

st.write(ans)





