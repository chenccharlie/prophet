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
    config = {
        SYMBOL: symbol,
        FUNCTION: function,
        API_KEY: configs.API_KEY,
    }
    config.update(FUNCTION_CONFIGS[function])
    return config


def _build_url(config):
    url = BASE_URL + '&'.join([key + '=' + config[key] for key in config])
    print "url", url
    return url


if __name__ == "__main__":
    for symbol in SYMBOLS:
        for function in FUNCTIONS:
            print "process", symbol, function
            config = _build_configs(symbol, function)
            url = _build_url(config)
            response = requests.get(url)
            print response.json()
