from function import Function

class BBANDS5Daily(Function):
  def get_name(self):
    return "BBANDS_5_DAILY"

  def get_function_name(self):
    return "BBANDS"

  def get_configs(self):
    return {
      "interval": "daily",
      "time_period": "5",
      "series_type": "close",
      "nbdevup": "3",
      "nbdevdn": "3",
    }

  def parse_data(self, data):
    daily_data = data["Technical Analysis: BBANDS"]
    daily_results = {
      "bbands5_lower_band": {},
      "bbands5_upper_band": {},
      "bbands5_middle_band": {},
    }
    dates = []

    for date in daily_data:
      daily_results["bbands5_lower_band"][date] = (
        daily_data[date]["Real Lower Band"]
      )
      daily_results["bbands5_upper_band"][date] = (
        daily_data[date]["Real Upper Band"]
      )
      daily_results["bbands5_middle_band"][date] = (
        daily_data[date]["Real Middle Band"]
      )
      dates.append(date)

    dates.sort()

    return {
      "dates": dates,
      "data": daily_results
    }
