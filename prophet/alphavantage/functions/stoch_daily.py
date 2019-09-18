from function import Function

class STOCHDaily(Function):
  def get_name(self):
    return "STOCH_DAILY"

  def get_function_name(self):
    return "STOCH"

  def get_configs(self):
    return {
      "interval": "daily",
    }

  def parse_data(self, data):
    daily_data = data["Technical Analysis: STOCH"]
    daily_results = {
      "stoch_slowk": {},
      "stoch_slowd": {},
    }
    dates = []

    for date in daily_data:
      daily_results["stoch_slowk"][date] = daily_data[date]["SlowK"]
      daily_results["stoch_slowd"][date] = daily_data[date]["SlowD"]
      dates.append(date)

    dates.sort()

    return {
      "dates": dates,
      "data": daily_results
    }
