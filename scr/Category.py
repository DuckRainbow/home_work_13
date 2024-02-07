from scr.Product import Product

class Category:
    title: str
    description: str
    goods: list

    def __init__(self, title, description, goods):
        self.title = title
        self.description = description
        self.goods = goods
        self.count = len(self.goods)
        self.unique = len(set(self.goods))

    # def display(self):

