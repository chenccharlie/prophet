import requests

from configs import *
from constants import *
from functions.time_series_daily import TimeSeriesDaily


SYMBOLS = ['MSFT']
FUNCTIONS = [TimeSeriesDaily()]


class Scraper:
  def scrape(self):
    for symbol in SYMBOLS:
      for function in FUNCTIONS:
        config = self._build_configs(symbol, function)
        url = self._build_url(config)
        response = requests.get(url)
        parsed_data = function.parse_data(response)
        return parsed_data

  def _build_configs(self, symbol, function):
    config = {
      SYMBOL: symbol,
      FUNCTION: function.get_name(),
      API_KEY: ALPHA_VANTAGE_API_KEY,
    }
    config.update(function.get_configs())
    return config

  def _build_url(self, config):
    url = BASE_URL + '&'.join([key + '=' + config[key] for key in config])
    return url
