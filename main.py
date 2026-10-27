#Stock Data Visualizer - main application

import os
from datetime import date

import requests
from dotenv import load_dotenv

from chart_generator import generate_chart

URL = "https://www.alphavantage.co/query"

Chart_Types = {"1": "bar", "2": "line"}
Time_Series = {"1": "TIME_SERIES_INTRADAY", "2": "TIME_SERIES_DAILY", "3": "TIME_SERIES_WEEKLY", "4": "TIME_SERIES_MONTHLY"}

Intraday_Interval = "5min"


def get_symbol():
    #asks for a stock symbol until a valid one is entered
    while True:
        symbol = input("Enter the stock symbol you are looking for: ").strip().upper()
        if symbol.replace(".", "").replace("-", "").isalnum():
            return symbol
        print("Please enter a valid stock symbol.\n")


def get_menu_choice(prompt, valid):
    #asks for a menu option from above until a valid one is entered
    while True:
        choice = input(prompt).strip()
        if choice in valid:
            return choice
        print(f"Invalid Choice. Please enter one of: {', '.join(valid)}\n")


def get_date(prompt):
    #asks for date until one is entered in valid format
    while True:
        text = input(prompt).strip()
        try:
            date.fromisoformat(text)
            if len(text) == 10:
                return text
        except ValueError:
            pass
        print("Invalid date. Please use the YYYY-MM-DD format.\n")


def get_end_date(start_date):
    #asks for a date after the start date
    while True:
        end_date = get_date("Enter the end date (YYYY-MM-DD): ")
        if date.fromisoformat(end_date) < date.fromisoformat(start_date):
            print("The end date cannot be before the start date.\n")
            continue
        return end_date


def fetch_stock_data(symbol, function, api_key):
    #query Alpha Vantage and return json response
    params = {"function": function, "symbol": symbol, "apikey": api_key, "outputsize": "full",}

    if function == "TIME_SERIES_INTRADAY":
        params["interval"] = Intraday_Interval

    response = requests.get(URL, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    #if outputsize=full cannot be used retry with compact
    if "Information" in data and "outputsize" in data["Information"].lower():
        params["outputsize"] = "compact"
        response = requests.get(URL, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

    return data


def check_api_errors(data):
    #Display an error if Alpha Vantage returns an error
    if "Error Message" in data:
        raise ValueError(f"Alpha Vantage returned and error: {data['Error Message']}")
    for key in ("Note", "Information"):
        if key in data:
            raise ValueError(f"Alpha Vantage says: {data[key]}")


def main():
    load_dotenv()
    api_key = os.getenv("AlPHA_VANTAGE_API_KEY")

    print("Stock Data Visualizer")
    print("-----------------------\n")

    symbol = get_symbol()

    print("\nChart Types")
    print("---------------\n")
    print("1. Bar")
    print("2. Line\n")
    chart_type = Chart_Types[get_menu_choice("Enter the chart type you want (1, 2): ", Chart_Types)]

    print("\n Select the Time Series of the chart you want to Generate")
    print("-------------------------------------------------------------\n")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly\n")
    function = Time_Series[get_menu_choice("Enter the time series option (1, 2, 3, 4): ", Time_Series)]

    print()
    start_date = get_date("Enter the starte Date (YYYY-MM-DD): ")
    print()
    end_date = get_end_date(start_date)

    try:
        data = fetch_stock_data(symbol, function, api_key)
        check_api_errors(data)
        generate_chart(data, symbol, chart_type, start_date, end_date)
    except requests.exceptions.RequestException as err:
        print(f"\nNetwork error while conecting to Alpha Vantage: {err}")
        return
    except ValueError as err:
        print(f"Error: {err}")
        return



if __name__ == "__main__":
    main()
