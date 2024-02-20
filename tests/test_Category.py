import unittest
from scr.Category import Category
from scr.Product import Product
from scr.classes_daughter import Smartphone, LawnGrass

soap = Product('Soap', 'just soap for hands', 50, 15)
spoon = Product('Spoon', 'spoon for soup', 120, 6)
knife = Product('Knife', 'just knife', 150, 4)
brush = Product('Brush', 'brush for cleaning smthng', 100, 12)
smth = 'smth??'
some_phone = Smartphone('title', 'description', '_price', 'quantity', 'performance', 'model', 'memory', 'color')
just_grass = LawnGrass('title', 'description', '_price', 'quantity', 'country', 'growing_time', 'color')


some_category = Category('home_apl', 'some goods for home', [soap, spoon, knife, brush])


class TestCategory(unittest.TestCase):

    def test_init(self):
        self.assertEqual(some_category.title, 'home_apl')
        self.assertEqual(some_category.description, 'some goods for home')
        self.assertEqual(some_category.goods,
                         ['Soap, 50руб. Остаток: 15 шт.', 'Spoon, 120руб. Остаток: 6 шт.',
                          'Knife, 150руб. Остаток: 4 шт.', 'Brush, 100руб. Остаток: 12 шт.'])

    def test_count(self):
        self.assertEqual(some_category.count, 1)

    def test_unique(self):
        self.assertEqual(some_category.unique, 4)

    def test_str(self):
        self.assertEqual(str(some_category), 'home_apl, количество продуктов: 4 шт.')

    def test_len(self):
        self.assertEqual(len(some_category), 4)
