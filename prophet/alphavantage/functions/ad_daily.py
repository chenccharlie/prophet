from function import Function

class ADDaily(Function):
  def get_name(self):
    return "AD_DAILY"

  def get_function_name(self):
    return "AD"

  def get_configs(self):
    return {
      "interval": "daily",
    }

  def parse_data(self, data):
    daily_data = data["Technical Analysis: Chaikin A/D"]
    daily_results = {
      "ad": {},
    }
    dates = []

    for date in daily_data:
      daily_results["ad"][date] = daily_data[date]["Chaikin A/D"]
      dates.append(date)

    dates.sort()

    return {
      "dates": dates,
      "data": daily_results
    }
