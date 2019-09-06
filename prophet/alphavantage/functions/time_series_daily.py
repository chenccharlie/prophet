import json

from function import Function

class TimeSeriesDaily(Function):
  def get_name():
    return "TIME_SERIES_DAILY"

  def get_configs():
    return {}

  def parse_data(json_data):
    data = json.load(json_data)
    last_refresh = data["Meta Data"]["3. Last Refreshed"]
    daily_data = data["Time Series (Daily)"]
    daily_results = {
      "open": {},
      "high": {},
      "low": {},
      "close": {},
      "volume": {},
    }
    dates = []

    for date in daily_data:
      daily_results["open"][date] = daily_data[date]["1. open"]
      daily_results["high"][date] = daily_data[date]["2. high"]
      daily_results["low"][date] = daily_data[date]["3. low"]
      daily_results["close"][date] = daily_data[date]["4. close"]
      daily_results["volume"][date] = daily_data[date]["5. volume"]

    dates.push_back(date)
    return {
      "dates": dates,
      "last_refresh": last_refresh,
      "data": daily_results
    }
