# Stock-Data-Visualizer

## Chart Generation (SDV-9)

Created a Python chart generator using Plotly and the Alpha Vantage API.

### Features
- Interactive line and bar charts
- Date range filtering
- Automatically opens charts in the browser

### Setup
Install the required libraries:

`py -m pip install -r requirements.txt`

Create a `.env` file containing:

`ALPHA_VANTAGE_API_KEY=your_key_here`

### Usage
Run `py test_chart.py` to test the charts with real stock data.

To use the chart generator in the main application:

`from chart_generator import generate_chart`

`generate_chart(stock_data, symbol, chart_type, start_date, end_date)`

Chart types: `"line"` or `"bar"`.

Dates must use `YYYY-MM-DD` format.
