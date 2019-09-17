from function import Function

class EMA10Daily(Function):
  def get_name(self):
    return "EMA_10_DAILY"

  def get_function_name(self):
    return "EMA"

  def get_configs(self):
    return {
      "interval": "daily",
      "time_period": "10",
      "series_type": "open"
    }

  def parse_data(self, data):
    daily_data = data["Technical Analysis: EMA"]
    daily_results = {
      "ema10": {},
    }
    dates = []

    for date in daily_data:
      daily_results["ema10"][date] = daily_data[date]["EMA"]
      dates.append(date)

    dates.sort()

    return {
      "dates": dates,
      "data": daily_results
    }
