import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
import pandas as pd
import datetime
import time

st.set_page_config(page_title="FinDash", layout="wide", page_icon="💸")
st.set_option("deprecation.showPyplotGlobalUse", False)

ticks = pd.read_csv("data/ticks.csv")
ticks = sorted(ticks.iloc[:]["Symbol"].tolist())

def load_data(ticker, start_date, end_date):
    data = yf.Ticker(ticker).history(start=start_date, end=end_date)
    return data

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

if load_status:
    with st.spinner(f"Loading {ticker} Data"):
        data = load_data(ticker, start_date, end_date)
        st.write(f"Let's view **{ticker}** from **{start_date}** to **{end_date}**. Here are the first 5 records.")
        st.table(data.head())
        with st.expander("View Candle Plot"):
            fig = go.Figure(
                data=[
                    go.Candlestick(
                        x=data.index,
                        open=data["Open"],
                        high=data["High"],
                        low=data["Low"],
                        close=data["Close"]
                    )
                ]
            )
            st.plotly_chart(fig, use_container_width=True)