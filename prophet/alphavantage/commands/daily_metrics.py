import os.path
import schedule

from os import path

from prophet.alphavantage.commands.base_command import BaseCommand
from prophet.alphavantage.functions.time_series_daily import TimeSeriesDaily
from prophet.alphavantage.scraper import Scraper


class DailyMetrics(BaseCommand):
  SYMBOLS = [
    "MSFT",
  ]
  FUNCTIONS = [
    TimeSeriesDaily(),
  ]
  BASE_DIR = (
    '/home/ccehshmily/github/prophet/prophet/alphavantage/data/daily_metrics'
  )

  def get_schedule(self, scheduler):
    print "Scheduled daily_metrics at 18:00 every day."
    return scheduler.every().day.at("18:00")

  def get_runnable(self):
    def run():
      for symbol in DailyMetrics.SYMBOLS:
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

        with open(
          '{}/{}.txt'.format(DailyMetrics.BASE_DIR, symbol),
          'a+',
        ) as file:
          for date in dates[start_index:]:
            file.write("{},{}\n".format(
              date,
              ",".join([data[label][date] for label in labels])),
            )
    return run
