import unittest
from scr.Product import Product

some_product = Product('Soap', 'soap for hands', 50, 15, 'color')
some_product_1 = Product('Spoon', 'spoon for soup', 120, 6, 'color')


class TestCategory(unittest.TestCase):

    def test_init(self):
        self.assertEqual(some_product.title, 'Soap')
        self.assertEqual(some_product.description, 'soap for hands')
        self.assertEqual(some_product.get_price, 50)
        self.assertEqual(some_product.quantity, 15)
        self.assertEqual(some_product.color, 'color')

    def test_create_product(self):
        self.assertTrue(isinstance(Product.create_product('Soap'), Product))

    def test_str(self):
        self.assertEqual(str(some_product), 'Soap, 50руб. Остаток: 15 шт.')

    def test_add(self):
        self.assertEqual(some_product + some_product_1, 1470)

