class Product:
    title: str
    description: str
    __price: float
    quantity: int

    def __init__(self, title, description, _price, quantity):
        self.title = title
        self.description = description
        self.__price = _price
        self.quantity = quantity

    @classmethod
    def create_product(cls, title, description, _price, quantity):
        """ Create and return new product """
        new_product = cls(title, description, _price, quantity)
        return new_product

    @property
    def get_price(self):
        return self.__price

    @get_price.setter
    def set_price(self, price):

        """ Set new price """
        if self.__price > price:
            unswer = input('New price is higher than old price. Confirm price change: enter yes(y) or no(n).')
            if unswer == 'y' or unswer == 'yes':
                self.__price = price
        elif price > 0:
            self.__price = price
        else:
            print('Incorrect price')

    def __str__(self):
        return f'{self.title}, {self.__price}. Remaining amount: {self.quantity} pcs.'

    def __add__(self, other):
        summ_ = self.__price * self.quantity + other.__price * other.quantity
        return summ_
