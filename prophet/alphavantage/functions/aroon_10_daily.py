from function import Function

class AROON10Daily(Function):
  def get_name(self):
    return "AROON_10_DAILY"

  def get_function_name(self):
    return "AROON"

  def get_configs(self):
    return {
      "interval": "daily",
      "time_period": "10",
    }

  def parse_data(self, data):
    daily_data = data["Technical Analysis: AROON"]
    daily_results = {
      "aroon10_up": {},
      "aroon10_down": {},
    }
    dates = []

    for date in daily_data:
      daily_results["aroon10_up"][date] = daily_data[date]["Aroon Up"]
      daily_results["aroon10_down"][date] = daily_data[date]["Aroon Down"]
      dates.append(date)

    dates.sort()

    return {
      "dates": dates,
      "data": daily_results
    }
