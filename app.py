import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px

# 1. Product Title & User Definition
st.title("📊 Corporate Financial Ratios Analyzer")
st.markdown("""
This tool is designed for **investors and accounting students** to analyze the financial health 
of public companies using real-time data from Yahoo Finance.
""")

# 2. Sidebar for User Input
st.sidebar.header("User Input Parameters")
ticker = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, MSFT, TSLA):", value="AAPL")
period = st.sidebar.selectbox("Select Period:", ["5y", "2y", "10y"])

if ticker:
    try:
        # 3. Data Acquisition
        stock = yf.Ticker(ticker)
        balance_sheet = stock.balance_sheet
        financials = stock.financials
        
        # 4. Substantive Data Transformation & Analysis
        # Extracting components for ROE (Net Income / Total Equity)
        net_income = financials.loc['Net Income']
        total_equity = balance_sheet.loc['Stockholders Equity']
        roe = (net_income / total_equity) * 100
        
        # Extracting Profit Margin (Net Income / Revenue)
        revenue = financials.loc['Total Revenue']
        profit_margin = (net_income / revenue) * 100

        # Create DataFrame for Visualization
        df_analysis = pd.DataFrame({
            'ROE (%)': roe,
            'Profit Margin (%)': profit_margin
        }).sort_index()

        # 5. Interactive Visualization
        st.subheader(f"Financial Performance: {ticker}")
        fig = px.line(df_analysis, x=df_analysis.index, y=['ROE (%)', 'Profit Margin (%)'],
                      labels={'value': 'Percentage (%)', 'index': 'Fiscal Year'},
                      title=f"Trends in Profitability for {ticker}")
        st.plotly_chart(fig)

        # 6. Key Insights Table
        st.write("### Data Summary Table")
        st.dataframe(df_analysis.style.format("{:.2f}%"))
        
        st.success(f"Analysis complete for {ticker}. The current ROE is {roe.iloc[0]:.2f}%.")

    except Exception as e:
        st.error(f"Error fetching data for {ticker}. Please ensure the ticker is correct.")
