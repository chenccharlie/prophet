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

  def setUp(self):
    self.scraper = Scraper()

  def test_scrape(self):
    self.assertEqual(
      self.scraper.scrape("MSFT")["data"].keys(),
      TestScraper.LABELS,
    )

if __name__ == '__main__':
    unittest.main()
