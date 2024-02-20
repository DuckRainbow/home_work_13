import unittest

from scr.classes_daughter import Smartphone, LawnGrass

some_phone = Smartphone('title', 'description', 10, 1, 'performance', 'model', 'memory', 'color')
some_phone1 = Smartphone('title', 'description', 20, 3, 'performance', 'model', 'memory', 'color')
some_grass = LawnGrass('title', 'description', 30, 2, 'country', 'growing_time', 'color')
some_grass2 = LawnGrass('title', 'description', 40, 4, 'country', 'growing_time', 'color')


class TestSmartphone(unittest.TestCase):

    def test_init(self):
        self.assertEqual(some_phone.title, 'title')
        self.assertEqual(some_phone.description, 'description')
        self.assertEqual(some_phone.get_price, 10)
        self.assertEqual(some_phone.quantity, 1)
        self.assertEqual(some_phone.performance, 'performance')
        self.assertEqual(some_phone.model, 'model')
        self.assertEqual(some_phone.color, 'color')
        self.assertEqual(some_phone.memory, 'memory')


class TestLawnGrass(unittest.TestCase):

    def test_init(self):
        self.assertEqual(some_grass.title, 'title')
        self.assertEqual(some_grass.description, 'description')
        self.assertEqual(some_grass.get_price, 30)
        self.assertEqual(some_grass.quantity, 2)
        self.assertEqual(some_grass.color, 'color')
        self.assertEqual(some_grass.country, 'country')
        self.assertEqual(some_grass.growing_time, 'growing_time')
