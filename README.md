# Corporate Financial Ratios Analyzer

##  [Click Here to View the Interactive Tool](https://4wswgdcpge8dvxqjwqmczr.streamlit.app/)
# Corporate Financial Ratios Analyzer

## 1. Problem & User
Analyzing complex financial statements is time-consuming for amateur investors. This tool provides an immediate interactive visualization of a company's ROE and Profit Margin to help users make quick investment decisions.

## 2. Data
- **Source:** Yahoo Finance (via `yfinance` library).
- **Access Date:** April 2026.
- **Key Fields:** Net Income, Total Revenue, Stockholders' Equity.

## 3. Methods
- **Cleaning:** Handling transposed financial matrices from the API.
- **Analysis:** Calculating financial ratios (ROE, Profit Margin) using Python arithmetic operations.
- **Visualization:** Interactive time-series charts using Plotly.

## 4. Key Findings
- Users can identify if a company's profitability is growing or declining over 5 years.
- The tool highlights the relationship between sales efficiency and shareholder returns.

## 5. Product Link
[Insert your Streamlit Cloud Link Here]

## 6. How to Run
1. Clone this repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run app: `streamlit run app.py`.

## 7. Limitations
- Relies on the availability of Yahoo Finance API.
- Only covers profitability ratios; liquidity and leverage ratios are not yet implemented.
