from function import Function

class MACDDaily(Function):
  def get_name(self):
    return "MACD_DAILY"

  def get_function_name(self):
    return "MACD"

  def get_configs(self):
    return {
      "interval": "daily",
      "series_type": "open"
    }

  def parse_data(self, data):
    daily_data = data["Technical Analysis: MACD"]
    daily_results = {
      "macd": {},
      "macd_hist": {},
      "macd_signal": {},
    }
    dates = []

    for date in daily_data:
      daily_results["macd"][date] = daily_data[date]["MACD"]
      daily_results["macd_hist"][date] = daily_data[date]["MACD_Hist"]
      daily_results["macd_signal"][date] = daily_data[date]["MACD_Signal"]
      dates.append(date)

    dates.sort()

    return {
      "dates": dates,
      "data": daily_results
    }
