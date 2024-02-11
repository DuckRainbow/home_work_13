import unittest
from scr.Product import Product

some_product = Product('soap', 'soap for hands', 250, 15)


class TestCategory(unittest.TestCase):

    def test_init(self):
        self.assertEqual(some_product.title, 'soap')
        self.assertEqual(some_product.description, 'soap for hands')
        self.assertEqual(some_product.price, 250)
        self.assertEqual(some_product.quantity, 15)