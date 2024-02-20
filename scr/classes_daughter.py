from scr.Product import Product


class Smartphone(Product):
    def __init__(self, title, description, _price, quantity, performance, model, memory, color):
        super().__init__(title, description, _price, quantity, color)
        self.performance = performance
        self.model = model
        self.memory = memory

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return super().__add__(self, other)

        raise TypeError


class LawnGrass(Product):
    def __init__(self, title, description, _price, quantity, country, growing_time, color):
        super().__init__(title, description, _price, quantity, color)
        self.country = country
        self.growing_time = growing_time

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return super().__add__(self, other)

        raise TypeError 
