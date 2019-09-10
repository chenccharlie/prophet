from function import Function

class TimeSeriesDaily(Function):
  def get_name(self):
    return "TIME_SERIES_DAILY"

  def get_configs(self):
    return {}

  def parse_data(self, data):
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
      dates.append(date)

    dates.sort(reverse=True)

    return {
      "dates": dates,
      "data": daily_results
    }
