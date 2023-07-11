import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']/quote['top_ask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price']/quote['top_ask']['price'])/2))
      
  """ ------------ Add more unit tests ------------ """
def test_getDataPoint_invalidQuote(self):
    quote = {'invalid_key': 'invalid_value'}  # Invalid quote without the necessary keys
    self.assertRaises(KeyError, getDataPoint, quote)

def test_getDataPoint_negativePrice(self):
    quote = {'top_ask': {'price': -10, 'size': 10}, 'top_bid': {'price': 20, 'size': 5}, 'stock': 'XYZ'}
    self.assertRaises(ValueError, getDataPoint, quote)

def test_getDataPoint_zeroAskPrice(self):
    quote = {'top_ask': {'price': 0, 'size': 10}, 'top_bid': {'price': 20, 'size': 5}, 'stock': 'XYZ'}
    self.assertRaises(ZeroDivisionError, getDataPoint, quote)

def test_getDataPoint_emptyStockName(self):
    quote = {'top_ask': {'price': 100, 'size': 10}, 'top_bid': {'price': 90, 'size': 5}, 'stock': ''}
    self.assertRaises(ValueError, getDataPoint, quote)


def test_getDataPoint_roundedPrice(self):
    quote = {'top_ask': {'price': 123.456, 'size': 10}, 'top_bid': {'price': 78.912, 'size': 5}, 'stock': 'XYZ'}
    self.assertEqual(getDataPoint(quote), ('XYZ', 78.912, 123.456, 0.3201244212063425))




if __name__ == '__main__':
    unittest.main()
