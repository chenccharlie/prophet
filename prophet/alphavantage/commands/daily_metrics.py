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

  def get_schedule(self, scheduler):
    print "schedule"
    return scheduler.every().minute
    # return scheduler.every().day.at("18:00")

  def get_runnable(self):
    print "get_run"
    def run():
      print "start"
      for symbol in DailyMetrics.SYMBOLS:
        scrape_result = self.scraper.scrape(symbol, DailyMetrics.FUNCTIONS)
        dates = scrape_result["dates"]
        data = scrape_result["data"]
        labels = list(data.keys())
        with open('../data/daily_metrics/{}'.format(symbol), 'w') as file:
          file.write("date,{}\n".format(labels.join(",")))
          for date in dates:
            file.write("{},{}\n".format(
              date,
              [data[label][date] for label in labels].join(",")),
            )
        file.flush()
        file.close()
      print "end"
    print "return run"
    return run
