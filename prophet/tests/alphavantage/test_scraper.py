import unittest

from prophet.alphavantage.scraper import Scraper

class TestScraper(unittest.TestCase):
  def setUp(self):
    self.scraper = Scraper()

  def test_scrape(self):
      self.assertEqual(self.scraper.scrape(), 'FOO')

if __name__ == '__main__':
    unittest.main()
