from function import Function

class RSI10Daily(Function):
  def get_name(self):
    return "RSI_10_DAILY"

  def get_function_name(self):
    return "RSI"

  def get_configs(self):
    return {
      "interval": "daily",
      "time_period": "10",
      "series_type": "open"
    }

  def parse_data(self, data):
    daily_data = data["Technical Analysis: RSI"]
    daily_results = {
      "rsi10": {},
    }
    dates = []

    for date in daily_data:
      daily_results["rsi10"][date] = daily_data[date]["RSI"]
      dates.append(date)

    dates.sort()

    return {
      "dates": dates,
      "data": daily_results
    }
