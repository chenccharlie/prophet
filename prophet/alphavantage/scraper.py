import requests
import time

from configs import *
from constants import *
from functions.time_series_daily import TimeSeriesDaily


class Scraper:
  def scrape(self, symbol, functions):
    dates = set([])
    data = {}
    for function in functions:
      print "Scrape {} for {}".format(function.get_name(), symbol)
      config = self._build_configs(symbol, function)
      url = self._build_url(config)
      response = requests.get(url)
      parsed_data = function.parse_data(response.json())
      dates.update(set(parsed_data["dates"]))
      data.update(parsed_data["data"])
      print "Rate limit: sleep 15 seconds..."
      time.sleep(15)

    dates = list(dates)
    dates.sort()
    return {
      "dates": dates,
      "data": data
    }

  def _build_configs(self, symbol, function):
    config = {
      SYMBOL: symbol,
      FUNCTION: function.get_function_name(),
      API_KEY: ALPHA_VANTAGE_API_KEY,
    }
    config.update(function.get_configs())
    return config

  def _build_url(self, config):
    url = BASE_URL + '&'.join([key + '=' + config[key] for key in config])
    return url
