#Charley Hamilton


from datetime import date, datetime
import plotly.graph_objects as go


def generate_chart(stock_data, symbol, chart_type, start_date, end_date, auto_open=True):

    # Convert the entered dates into Python dates
    start = date.fromisoformat(start_date)
    end = date.fromisoformat(end_date)

    # Make sure the date range is valid
    if start > end:
        raise ValueError("Start date cannot be after end date.")

    # Find the stock prices in the Alpha Vantage response
    time_series = next(
        (value for key, value in stock_data.items()
         if "time series" in key.lower() and isinstance(value, dict)),
        None
    )

    if not time_series:
        raise ValueError("No stock data found in the API response.")

    points = []
 
    # Get closing prices within the selected date range
    for stamp, values in time_series.items():
        # Intraday keys include a time ("2020-08-03 15:55:00"); others are dates only
        moment = datetime.fromisoformat(stamp)
 
        if start <= moment.date() <= end:
            points.append((moment, float(values["4. close"])))
 
    if not points:
        raise ValueError("No stock data available for these dates.")
 
    # Sort the data chronologically
    points.sort()
    dates, prices = zip(*points)
 
    # Generate the user's selected chart type
    chart_type = chart_type.lower().strip()
 
    if chart_type == "line":
        chart = go.Scatter(x=dates, y=prices, mode="lines+markers")
    elif chart_type == "bar":
        chart = go.Bar(x=dates, y=prices)
    else:
        raise ValueError("Chart type must be 'line' or 'bar'.")
 
    # Customize the chart
    fig = go.Figure(data=[chart])
 
    fig.update_layout(
        title=f"{symbol.upper()} Stock Prices ({start_date} to {end_date})",
        xaxis_title="Date",
        yaxis_title="Closing Price (USD)",
        template="plotly_white",
        hovermode="x unified"
    )

    # Save and open the chart in the user's browser
    fig.write_html("stock_chart.html", auto_open=auto_open)
