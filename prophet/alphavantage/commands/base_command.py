from prophet.alphavantage.scraper import Scraper


class BaseCommand:
  def __init__(self):
    self.scraper = Scraper()

  def get_schedule(self, scheduler):
    raise NotImplementedError

  def get_runnable(self):
    raise NotImplementedError
