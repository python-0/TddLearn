import unittest
from datetime import datetime

from src.stock import Stock


class StockTest(unittest.TestCase):
	def test_price_should_be_null(self):
		stock = Stock("GooG")

		self.assertIsNone(stock.price)

	def test_stock_update(self):
		goog = Stock("GooG")
		goog.update(datetime(2014, 2, 12), 10)
		self.assertEqual(10, goog.price)

	def test_negative_price_should_throw_ValueError(self):
		goog = Stock("GooG")
		with self.assertRaises(ValueError):
			goog.update(datetime(2014, 2, 3), -1)


