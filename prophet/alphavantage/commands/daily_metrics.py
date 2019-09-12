import schedule

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
    return scheduler.every(5).seconds
    # return scheduler.every().day.at("18:00")

  def get_runnable(self):
    def run():
      for symbol in DailyMetrics.SYMBOLS:
        scrape_result = self.scraper.scrape(symbol, DailyMetrics.FUNCTIONS)
        dates = scrape_result["dates"]
        data = scrape_result["data"]
        labels = list(data.keys())
        with open(
          '{}/{}.txt'.format(DailyMetrics.BASE_DIR, symbol),
          'w+',
        ) as file:
          file.write("date,{}\n".format(",".join(labels)))
          for date in dates:
            file.write("{},{}\n".format(
              date,
              ",".join([data[label][date] for label in labels])),
            )
    return run
