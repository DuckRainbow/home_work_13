import unittest
from scr.Category import Category
from scr.Product import Product

soap = Product('Soap', 'just soap for hands', 50, 15)
spoon = Product('Spoon', 'spoon for soup', 120, 6)
knife = Product('Knife', 'just knife', 150, 4)
brush = Product('Brush', 'brush for cleaning smthng', 100, 12)

some_category = Category('home_apl', 'some goods for home', [soap, spoon, knife, brush])


class TestCategory(unittest.TestCase):

    def test_init(self):
        self.assertEqual(some_category.title, 'home_apl')
        self.assertEqual(some_category.description, 'some goods for home')
        self.assertEqual(some_category.goods,
                         ['Soap, 50. Remaining amount: 15 pcs.', 'Spoon, 120. Remaining amount: 6 pcs.',
                          'Knife, 150. Remaining amount: 4 pcs.', 'Brush, 100. Remaining amount: 12 pcs.'])

    def test_count(self):
        self.assertEqual(some_category.count, 1)

    def test_unique(self):
        self.assertEqual(some_category.unique, 4)

    def test_str(self):
        self.assertEqual(str(some_category), 'home_apl, quantity of products: 4 pcs.')

    def test_len(self):
        self.assertEqual(len(some_category), 4)
