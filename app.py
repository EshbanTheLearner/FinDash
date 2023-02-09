import streamlit as st
import yfinance as yf
import mplfinance as mpf
import pandas as pd
import datetime
import time

st.set_page_config(page_title="FinDash", layout="wide", page_icon="💸")

ticks = pd.read_csv("data/ticks.csv")
ticks = sorted(ticks.iloc[:]["Symbol"].tolist())

def load_data(ticker, start_date, end_date):
    time.sleep(5)
    st.write(f"Let's view **{ticker}** from **{start_date}** to **{end_date}**")

with st.sidebar:
    st.subheader("FinDash 💸")
    ticker = st.selectbox("Select a Stock", ticks)
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("From", datetime.date(2023, 1, 1))
    with col2:
        end_date = st.date_input("To", datetime.datetime.today())

    load_status = st.button(f"Analyze {ticker} Data")

st.header("FinDash 💸")
#st.write(f"Let's view **{ticker}** from **{start_date}** to **{end_date}**")

if load_status:
    with st.spinner(f"Loading {ticker} Data"):
        load_data(ticker, start_date, end_date)