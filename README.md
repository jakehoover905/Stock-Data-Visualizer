# Stock-Data-Visualizer
A Python app that pulls stock data from the Alpha Vantage API, Let's you choose a date range, chart type, and time series, and opens a chart in your browser

## Features
- Interactive line and bar charts
- Intraday, Daily, Weekly, and Monthly time series
- date range filtering
- Automatically opens charts in the browser

### Setup
1. Get a free API key at https://www.alphavantage.co/support/#api-key
2. Install the requirements
    Windows: py -m pip install -r requirements.txt
    MacOS/Linux: python3 -m pip install -r requirements.txt
3. Create a .env file containing: ALPHA_VANTAGE_API_KEY=your_key_here
4. replace "your_key_here" with your API key

### Usage
To run application: 
    Windows: py main.py
    MacOS/Linux: python3 main.py

You will be asked:
1. Stock symbol (e.g. GOOGL)
2. Chart type: 1 = bar, 2 = line
3. Time series: 1 = Intraday, 2 = Daily, 3 = Weekly, 4 = Monthly
4. Start Date(YYYY-MM-DD)
5. End Date(YYYY-MM-DD)

### Notes
With the free API key only allows recent data for intraday and daily time series.
