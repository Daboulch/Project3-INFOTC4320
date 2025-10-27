import pygal
import lxml
import requests
from datetime import datetime

def get_symbol():
    symbol = input("Enter the stock symbol (e.g., AAPL, TSLA, MSFT): ").upper().strip()
    return symbol


def get_chart():
    print("\nChoose a chart type:")
    print("1. Line")
    print("2. Bar")
    print("3. Candlestick")
    chart_choice = input("Enter your choice (1-3): ").strip()

    if chart_choice == "1":
        chart_type = "line"
    elif chart_choice == "2":
        chart_type = "bar"
    elif chart_choice == "3":
        chart_type = "candlestick"
    else:
        print("Invalid choice, defaulting to line chart.")
        chart_type = "line"

    return chart_type


def get_time_series():
    print("\nChoose a time series function:")
    print("1. TIME_SERIES_INTRADAY")
    print("2. TIME_SERIES_DAILY")
    print("3. TIME_SERIES_WEEKLY")
    print("4. TIME_SERIES_MONTHLY")
    time_choice = input("Enter your choice (1-4): ").strip()

    if time_choice == "1":
        time_series = "TIME_SERIES_INTRADAY"
    elif time_choice == "2":
        time_series = "TIME_SERIES_DAILY"
    elif time_choice == "3":
        time_series = "TIME_SERIES_WEEKLY"
    elif time_choice == "4":
        time_series = "TIME_SERIES_MONTHLY"
    else:
        print("Invalid choice, defaulting to TIME_SERIES_DAILY.")
        time_series = "TIME_SERIES_DAILY"

    return time_series


def get_date():
#Pranya
    return()


def get_data(symbol, start_date, end_date, api_key, function):  
    url = "https://www.alphavantage.co/query"
    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key,
        "outputsize": "full",
    }

    TIME_SERIES_KEYS = {
        "TIME_SERIES_INTRADAY": "Time Series (5min)",
        "TIME_SERIES_DAILY": "Time Series (Daily)",
        "TIME_SERIES_WEEKLY": "Weekly Time Series",
        "TIME_SERIES_MONTHLY": "Monthly Time Series",
    }

    if function == "TIME_SERIES_INTRADAY":
        params["interval"] = "5min"

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    key_check = TIME_SERIES_KEYS.get(function)
    if "Error Message" in data:
        raise ValueError(f"API returned an error: {data['Error Message']}")
    if not key_check or key_check not in data:
        raise ValueError(f"No time series data found. Response: {data}")
    
    raw_data = data[TIME_SERIES_KEYS[function]]

    filtered_data = {
        date: values
        for date, values in raw_data.items()
        if start_date <= date <= end_date
    }

    sorted_data = dict(sorted(filtered_data.items()))
    
    return sorted_data


example = "false"
if example == "true":
    api_key = "EDR5KNC8XVI980TW"
    function = "TIME_SERIES_INTRADAY"
    symbol = "AAPL"
    start_date = "2025-08-25"
    end_date = "2025-09-30"

try:
    stock_data = get_data(symbol, start_date, end_date, api_key, function)
    print(f"Data for {symbol} using {function} from {start_date} to {end_date}")
    for date, values in stock_data.items():
        print(f"{date} | Open: {values['1. open']} | High: {values['2. high']} | Low: {values['3. low']} | Close: {values['4. close']}")
except ValueError as e:
    print(e)


def create_graph():
#Pranya
    return()
