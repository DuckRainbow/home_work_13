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
        Category.unique += len(set(self.goods))

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
        self.__goods.append(good)

    def __str__(self):
        return f'{self.title}, quantity of products: {len(self)} pcs.'

    def __len__(self):
        self.length = len(self.__goods)
        return self.length
