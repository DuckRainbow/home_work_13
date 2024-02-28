from scr.base_abc_class import SomeProduct
from scr.mixing_class import MixingLog


class Product(MixingLog, SomeProduct):
    title: str
    description: str
    __price: float
    quantity: int
    color: str

    def __init__(self, title, description, _price, quantity, color):
        self.title = title
        self.description = description
        self.__price = _price
        self.quantity = quantity
        self.color = color
        super().__init__()

    @classmethod
    def create_product(cls, title, description, _price, quantity, color):
        """ Create and return new product """
        new_product = cls(title, description, _price, quantity, color)
        return new_product

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def set_price(self, price, interactive=True):
        """ Set new price """
        if self.__price > price and interactive:
            unswer = input('New price is higher than old price. Confirm price change: enter yes(y) or no(n).')
            if unswer.lower() in ['y', 'yes']:
                self.__price = price
        elif price > 0:
            self.__price = price
        else:
            print('Incorrect price')

    def __str__(self):
        return f'{self.title}, {self.__price}руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        summ_ = self.__price * self.quantity + other.__price * other.quantity
        return summ_
