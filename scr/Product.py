class Product:
    title: str
    description: str
    price: float
    quantity: int

    def __init__(self, title, description, price, quantity):
        self.title = title
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def create_product(cls, title, description, price, quantity):
        """ Create and return new product """
        new_product = cls(title, description, price, quantity)
        return new_product

    @property
    def product_price(self):
        return self.__price

    @product_price.setter
    def new_price(self, price):
        """ Set new price """
        if self.__price > price:
            unswer = input('New price is higher than old price. Confirm price change: enter yes(y) or no(n).')
            if unswer == 'y' or unswer == 'yes':
                self.__price = price
