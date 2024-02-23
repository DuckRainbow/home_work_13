from scr.Product import Product
from scr.base_abc_class import SomeProduct


class Smartphone(SomeProduct, Product):
    def __init__(self, title, description, _price, quantity, performance, model, memory, color):
        super().__init__(title, description, _price, quantity, color)
        self.performance = performance
        self.model = model
        self.memory = memory

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return super().__add__(self)

        raise TypeError


class LawnGrass(SomeProduct, Product):
    def __init__(self, title, description, _price, quantity, country, growing_time, color):
        super().__init__(title, description, _price, quantity, color)
        self.country = country
        self.growing_time = growing_time

    def __add__(self, other):
        if isinstance(other, LawnGrass):
            return super().__add__(self)

        raise TypeError 
