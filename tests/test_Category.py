import unittest
from scr.Category import Category

some_category = Category('home_apl', 'some goods for home', ['soap', 'spoon', 'knife', 'spoon', 'brush'])


class TestCategory(unittest.TestCase):

    def test_init(self):
        self.assertEqual(some_category.title, 'home_apl')
        self.assertEqual(some_category.description, 'some goods for home')
        self.assertEqual(some_category.goods, ['soap', 'spoon', 'knife', 'spoon', 'brush'])

    def test_count(self):
        self.assertEqual(some_category.count, 1)

    def test_unique(self):
        self.assertEqual(some_category.unique, 4)

    # def __init__(self, title, description, goods):
    #     self.title = title
    #     self.description = description
    #     self.goods = goods
    #     self.count = len(self.goods)
    #     self.unique = len(set(self.goods))
