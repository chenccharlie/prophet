from function import Function

class OBVDaily(Function):
  def get_name(self):
    return "OBV_DAILY"

  def get_function_name(self):
    return "OBV"

  def get_configs(self):
    return {
      "interval": "daily",
    }

  def parse_data(self, data):
    daily_data = data["Technical Analysis: OBV"]
    daily_results = {
      "obv": {},
    }
    dates = []

    for date in daily_data:
      daily_results["obv"][date] = daily_data[date]["OBV"]
      dates.append(date)

    dates.sort()

    return {
      "dates": dates,
      "data": daily_results
    }
