from constants import *

import configs
import requests


SYMBOLS = ['MSFT']
FUNCTIONS = ['TIME_SERIES_INTRADAY']
FUNCTION_CONFIGS = {
    'TIME_SERIES_INTRADAY': {
        INTERVAL: '5min',
    }
}


def _build_configs(symbol, function):
    return {
        SYMBOL: symbol,
        FUNCTION: function,
        API_KEY: configs.API_KEY,
    } + FUNCTION_CONFIGS[function]


def _build_url(config):
    return BASE_URL + [key + '=' + value for key, value in config].join('&')


def __main__():
    for symbol in SYMBOLS:
        for function in functions:
            config = _build_configs(symbol, function)
            url = _build_url(config)
            response = requests.get(url)
            print response.json()
