visit https://etf-dividend-calculator-rzj2rxrooatbgeune8gkyz.streamlit.app/ to test it out via web application

Overview
This repository contains a small Streamlit application for simulating dividend reinvestment.
Key elements:

app.py – main Streamlit script.

Optionally pulls live price/dividend data from Yahoo Finance (yfinance).

Accepts manual inputs for initial investment, price, dividend per share, payout frequency, and simulation length (in weeks).

Simulates dividend reinvestment over time, tracking shares and portfolio value.

Displays results in a table and line chart (pandas + matplotlib).

Allows downloading the breakdown as CSV.

requirements.txt – runtime dependencies: streamlit, yfinance, pandas, matplotlib.

.devcontainer/devcontainer.json – VS Code/Dev Container configuration for running the app with Streamlit.

README.md – link to a deployed Streamlit instance.

Structure & Flow
App setup: Streamlit title, optional ticker input.

Data acquisition:

If ticker is provided, yfinance.Ticker retrieves latest price and dividend info.

Otherwise, defaults are used.

User inputs: initial investment, price, dividend per share, dividend frequency, simulation duration, and view mode (weekly/yearly).

Simulation loop:

For each week, add dividends (depending on frequency), reinvest into additional shares, compute portfolio value.

Output:

Table (weekly/yearly) via st.dataframe.

Line chart using matplotlib rendered with st.pyplot.

CSV download button.

Key Concepts & Libraries
Streamlit: building web interfaces with widgets (st.checkbox, st.number_input, st.selectbox, etc.).

pandas: data manipulation, grouping, and CSV export.

yfinance: fetching market data.

matplotlib: basic plotting in Streamlit.

Suggested Next Steps
Learn Streamlit basics

Widgets, session state, layout, and forms.

Explore multi-page apps or reusable components.

Deepen data handling

pandas for more complex aggregations, plotting, and time-series handling.

External data sources

Explore yfinance capabilities: historical data, multiple tickers, caching, rate-limiting.

Code organization

Refactor app.py into functions/modules, add docstrings, and include tests (e.g., via pytest).

Feature expansion ideas

Variable dividend rates, taxation effects, DRIP vs. cash dividends, comparisons between tickers/strategies, multi-asset portfolios.

This codebase is a straightforward starting point: one file, minimal dependencies, and clear data flow. It’s ideal for newcomers exploring Python web apps and basic financial simulations.
