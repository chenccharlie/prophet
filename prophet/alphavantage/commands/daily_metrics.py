import os.path
import schedule

from os import path

from prophet.alphavantage.commands.base_command import BaseCommand
from prophet.alphavantage.functions.ad_daily import ADDaily
from prophet.alphavantage.functions.adx_10_daily import ADX10Daily
from prophet.alphavantage.functions.aroon_10_daily import AROON10Daily
from prophet.alphavantage.functions.bbands_5_daily import BBANDS5Daily
from prophet.alphavantage.functions.cci_10_daily import CCI10Daily
from prophet.alphavantage.functions.ema_10_daily import EMA10Daily
from prophet.alphavantage.functions.macd_daily import MACDDaily
from prophet.alphavantage.functions.obv_daily import OBVDaily
from prophet.alphavantage.functions.rsi_10_daily import RSI10Daily
from prophet.alphavantage.functions.sma_10_daily import SMA10Daily
from prophet.alphavantage.functions.stoch_daily import STOCHDaily

from prophet.alphavantage.functions.time_series_daily import TimeSeriesDaily

from prophet.alphavantage.scraper import Scraper


class DailyMetrics(BaseCommand):
  FUNCTIONS = [
    TimeSeriesDaily(),
    ADDaily(),
    ADX10Daily(),
    AROON10Daily(),
    BBANDS5Daily(),
    CCI10Daily(),
    EMA10Daily(),
    MACDDaily(),
    OBVDaily(),
    RSI10Daily(),
    SMA10Daily(),
    STOCHDaily(),
  ]
  ALPHAVANTAGE_DIR = '/home/ccehshmily/github/prophet/prophet/alphavantage'
  BASE_DIR = ALPHAVANTAGE_DIR + '/data/daily_metrics'

  def get_schedule(self, scheduler):
    print "Scheduled daily_metrics at 18:00 every day."
    return scheduler.every().day.at("18:00")

  def get_runnable(self):
    def run():
      symbols_file = open(DailyMetrics.ALPHAVANTAGE_DIR + '/symbols.txt', 'r')
      symbols = [
        symbol[:-1]
        for symbol in symbols_file.readlines()
      ]
      for symbol in symbols:
        scrape_result = self.scraper.scrape(symbol, DailyMetrics.FUNCTIONS)
        dates = scrape_result["dates"]
        data = scrape_result["data"]
        labels = list(data.keys())
        start_index = 0

        if not path.exists('{}/{}.txt'.format(DailyMetrics.BASE_DIR, symbol)):
          with open(
            '{}/{}.txt'.format(DailyMetrics.BASE_DIR, symbol),
            'w+',
          ) as file:
            file.write("date,{}\n".format(",".join(labels)))

        with open(
          '{}/{}.txt'.format(DailyMetrics.BASE_DIR, symbol),
          'r',
        ) as file:
          lines = file.readlines()
          if len(lines) > 1:
            last_recorded_date = lines[-1].split(",")[0]
            start_index = dates.index(last_recorded_date) + 1

        skipped_dates = []
        with open(
          '{}/{}.txt'.format(DailyMetrics.BASE_DIR, symbol),
          'a+',
        ) as file:
          for date in dates[start_index:]:
            if len(date) != 10:
              skipped_dates.append(date)
              continue
            try:
              file.write("{},{}\n".format(
                date,
                ",".join([data[label][date] for label in labels])),
              )
            except KeyError:
              # Skip writing the date when not all values can be found
              skipped_dates.append(date)
        print("Finished daily_metrics run for {}, skipped dates: {}".format(
          symbol, skipped_dates))
    return run
