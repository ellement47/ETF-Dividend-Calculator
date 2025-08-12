import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# App title
st.title("Dividend Reinvestment Calculator")
st.subheader("Created by : Lucas Payne")

# Ticker input (optional)
use_ticker = st.checkbox("Pull live data from a stock ticker")

# Defaults
stock_price = 10.0
dividend_per_share = 0.17

if use_ticker:
    ticker_symbol = st.text_input("Enter Stock Ticker (e.g., AAPL, O, QYLD)", value="AAPL")
    try:
        ticker_data = yf.Ticker(ticker_symbol)
        hist = ticker_data.history(period="1d")
        stock_price = hist["Close"].iloc[-1]
        info = ticker_data.info
        dividend_rate = info.get("dividendRate")
        dividend_per_share = (dividend_rate / 4) if dividend_rate else 0.0  # Estimated quarterly dividend
        st.success(
            f"Loaded: {ticker_symbol.upper()} | Price: ${stock_price:.2f} | Est. Dividend: ${dividend_per_share:.2f}"
        )
    except Exception as e:
        st.warning(f"Could not fetch data for {ticker_symbol.upper()}: {e}")

# User input section
initial_investment = st.number_input("Initial Investment ($)", min_value=0.0, value=1000.0)
stock_price = st.number_input("Stock Price ($)", min_value=0.01, value=stock_price)
dividend_per_share = st.number_input("Dividend Per Share ($)", min_value=0.0, value=dividend_per_share)

frequency = st.selectbox("Dividend Frequency", options=["Weekly", "Biweekly", "Monthly", "Quarterly"])
weeks = st.number_input("Simulation Duration (in Weeks)", min_value=1, value=104)  # 2 years by default
view_mode = st.radio("View breakdown by:", ["Weekly", "Yearly"])

# Map dividend frequency to payout interval in weeks
frequency_to_weeks = {
    "Weekly": 1,
    "Biweekly": 2,
    "Monthly": 4,
    "Quarterly": 13
}
div_interval = frequency_to_weeks[frequency]

# Simulation
shares = initial_investment / stock_price
data = []

for week in range(1, weeks + 1):
    if week % div_interval == 0:
        dividend = shares * dividend_per_share
        shares += dividend / stock_price
    portfolio_value = shares * stock_price
    data.append({
        "Week": week,
        "Year": (week - 1) // 52 + 1,
        "Shares": shares,
        "Portfolio Value": portfolio_value
    })

df = pd.DataFrame(data)

# View Mode: Weekly or Yearly
if view_mode == "Weekly":
    display_df = df[["Week", "Shares", "Portfolio Value"]]
    x_axis = "Week"
else:
    display_df = df.groupby("Year").agg({
        "Shares": "last",
        "Portfolio Value": "last"
    }).reset_index()
    x_axis = "Year"

# Display table
st.subheader(f"{view_mode} Portfolio Breakdown")
st.dataframe(display_df.style.format({
    "Shares": "{:.4f}",
    "Portfolio Value": "${:,.2f}"
}))

# Plot
st.subheader(f"Portfolio Value ({view_mode})")
fig, ax = plt.subplots()
ax.plot(display_df[x_axis], display_df["Portfolio Value"], marker='o', label="Portfolio Value")
ax.set_xlabel(x_axis)
ax.set_ylabel("Value ($)")
ax.set_title("Dividend Reinvestment Growth")
ax.grid(True)
st.pyplot(fig)

# Download CSV
csv = display_df.to_csv(index=False).encode("utf-8")
st.download_button("Download CSV", csv, f"dividend_breakdown_{view_mode.lower()}.csv", "text/csv")
