from function import Function

class SMA10Daily(Function):
  def get_name(self):
    return "SMA_10_DAILY"

  def get_function_name(self):
    return "SMA"

  def get_configs(self):
    return {
      "interval": "daily",
      "time_period": "10",
      "series_type": "open"
    }

  def parse_data(self, data):
    daily_data = data["Technical Analysis: SMA"]
    daily_results = {
      "sma10": {},
    }
    dates = []

    for date in daily_data:
      daily_results["sma10"][date] = daily_data[date]["SMA"]
      dates.append(date)

    dates.sort()

    return {
      "dates": dates,
      "data": daily_results
    }
