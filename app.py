import pygal
import lxml
import requests
from datetime import datetime

def get_symbol():
#Blake
    return ()

def get_chart():
#Blake
    return ()

def get_time_series():
#Blake
    return()

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

        #Requesting for data
        response = requests.get(url, params=params)
        #HTTP error check
        response.raise_for_status()
        #Convert JSON data to a dictionary
        data=response.json()

        #Check for errors or if rate limit is reached (Only 25 requests per day)
        key_check = TIME_SERIES_KEYS.get(function)
        if "Error Message" in data:
            raise ValueError(f"API returned an error: {data['Error Message']}")
        if not key_check or key_check not in data:
            raise ValueError(f"No time series data found. Response: {data}")
        
        #Filtering data to selected time frame and sorting data
        raw_data = data[TIME_SERIES_KEYS[function]]

        filtered_data = {
            date: values
            for date, values in raw_data.items()
            if start_date <= date <= end_date
        }

        sorted_data = dict(sorted(filtered_data.items()))
        
        return sorted_data

#Example input data to test output, change to whatever you want to test and set example = "true". Max of 25 API requests per day
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
