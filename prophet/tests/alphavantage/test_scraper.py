import unittest

from prophet.alphavantage.scraper import Scraper

class TestScraper(unittest.TestCase):
  LABELS = [
    "open",
    "high",
    "low",
    "close",
    "volume",
  ]

  SYMBOL = "MSFT"
  FUNCTIONS = [TimeSeriesDaily(),]

  def setUp(self):
    self.scraper = Scraper()

  def test_scrape(self):
    self.assertEqual(
      set(
        self.scraper.scrape(
          TestScraper.SYMBOL,
          TestScraper.FUNCTIONS,
        )["data"].keys(),
      ),
      set(TestScraper.LABELS),
    )

if __name__ == '__main__':
    unittest.main()
