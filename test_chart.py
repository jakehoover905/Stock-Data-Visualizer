#Testing script for the stock chart generator
#Charley Hamilton

import os
import requests
from datetime import date, timedelta
from dotenv import load_dotenv
from chart_generator import generate_chart

# Load the API key from the .env file
load_dotenv()
api_key = os.getenv("ALPHA_VANTAGE_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check your .env file.")

# Select the stock to retrieve
symbol = "IBM"

# Configure the Alpha Vantage API request
url = "https://www.alphavantage.co/query"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": symbol,
    "apikey": api_key
}

# Request stock prices from the API
print("Fetching stock data...")

response = requests.get(url, params=parameters, timeout=30)
response.raise_for_status()
stock_data = response.json()

# Check that valid stock data was returned
if "Time Series (Daily)" not in stock_data:
    message = (
        stock_data.get("Information")
        or stock_data.get("Note")
        or stock_data.get("Error Message")
        or "Unknown API response"
    )
    raise ValueError(f"API error: {message}")

# Select the most recent 30 calendar days
end_date = date.today()
start_date = end_date - timedelta(days=30)

print("Generating stock chart...")

# Call the chart generator you created
generate_chart(
    stock_data,
    symbol,
    "line",
    start_date.isoformat(),
    end_date.isoformat()
)

print("Success! Your stock chart should open in your browser.")
