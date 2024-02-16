import unittest
from scr.Category import Category

some_category = Category('home_apl', 'some goods for home', ['soap', 'spoon', 'knife', 'spoon', 'brush'])


class TestCategory(unittest.TestCase):

    def test_init(self):
        self.assertEqual(some_category.title, 'home_apl')
        self.assertEqual(some_category.description, 'some goods for home')

    def test_count(self):
        self.assertEqual(some_category.count, 1)

    def test_unique(self):
        self.assertEqual(some_category.unique, 4)

    def test_str(self):
        self.assertEqual(str(some_category), 'home_apl, quantity of products: 5 pcs.')

    def test_len(self):
        self.assertEqual(len(some_category), 5)