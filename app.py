import streamlit as st
import yfinance as yf
import mplfinance as mpf
import pandas as pd

st.set_page_config(page_title="FinDash", layout="wide", page_icon="💸")

ticks = pd.read_csv("data/ticks.csv", header=None)
ticks = sorted(ticks.iloc[:][0].tolist())

with st.sidebar:
    st.subheader("Select a Stock")
    ticker = st.selectbox("Select a stock", ticks)

st.header("FinDash 💸")
st.write(f"You selected: {ticker}")