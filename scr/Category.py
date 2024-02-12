from scr.Product import Product


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
        for good in self.__goods:
            return f'{good.title}, {good.price} руб. Остаток: {good.quantity} шт.'

    @goods.setter
    def add_good(self, good):
        """ Add product in list """
        self.__goods.append(good)
