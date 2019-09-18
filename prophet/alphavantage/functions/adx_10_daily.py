from function import Function

class ADX10Daily(Function):
  def get_name(self):
    return "ADX_10_DAILY"

  def get_function_name(self):
    return "ADX"

  def get_configs(self):
    return {
      "interval": "daily",
      "time_period": "10",
    }

  def parse_data(self, data):
    daily_data = data["Technical Analysis: ADX"]
    daily_results = {
      "adx10": {},
    }
    dates = []

    for date in daily_data:
      daily_results["adx10"][date] = daily_data[date]["ADX"]
      dates.append(date)

    dates.sort()

    return {
      "dates": dates,
      "data": daily_results
    }
