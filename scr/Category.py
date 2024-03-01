from scr.Product import Product


# noinspection PyPropertyDefinition
class Category:
    title: str
    description: str
    goods: list

    count = 0
    unique = 0

    def __init__(self, title, description, goods):
        self.title = title
        self.description = description
        self.__goods = goods

        Category.count += 1
        Category.unique += len(set(self.__goods))

    @property
    def goods(self):
        """ Return title, price and quantity of every product"""
        list_goods = []
        for good in self.__goods:
            list_goods.append(str(good))
        return list_goods

    @goods.setter
    def add_good(self, good):
        """ Add product in list """
        if isinstance(good, Product):
            self.__goods.append(good)
        else:
            raise TypeError

    def __str__(self):
        return f'{self.title}, количество продуктов: {len(self)} шт.'

    def __len__(self):
        self.length = len(self.__goods)
        return self.length

    def middle_price(self, summ_of_prices=None):
        for product in self.__goods:
            summ_of_prices += product.get_price
        try:
            return summ_of_prices / len(self.__goods)
        except ZeroDivisionError:
            return 0
