import requests

from configs import *
from constants import *


SYMBOLS = ['MSFT']
FUNCTIONS = ['TIME_SERIES_INTRADAY']
FUNCTION_CONFIGS = {
    'TIME_SERIES_INTRADAY': {
        INTERVAL: '5min',
    }
}


def _build_configs(symbol, function):
    config = {
        SYMBOL: symbol,
        FUNCTION: function,
        API_KEY: ALPHA_VANTAGE_API_KEY,
    }
    config.update(FUNCTION_CONFIGS[function])
    return config


def _build_url(config):
    url = BASE_URL + '&'.join([key + '=' + config[key] for key in config])
    return url


def scrape():
    for symbol in SYMBOLS:
        for function in FUNCTIONS:
            config = _build_configs(symbol, function)
            url = _build_url(config)
            response = requests.get(url)

scrape()
