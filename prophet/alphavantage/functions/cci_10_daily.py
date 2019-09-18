from function import Function

class CCI10Daily(Function):
  def get_name(self):
    return "CCI_10_DAILY"

  def get_function_name(self):
    return "CCI"

  def get_configs(self):
    return {
      "interval": "daily",
      "time_period": "10",
    }

  def parse_data(self, data):
    daily_data = data["Technical Analysis: CCI"]
    daily_results = {
      "cci10": {},
    }
    dates = []

    for date in daily_data:
      daily_results["cci10"][date] = daily_data[date]["CCI"]
      dates.append(date)

    dates.sort()

    return {
      "dates": dates,
      "data": daily_results
    }
