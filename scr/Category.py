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
        self.goods = goods

        Category.count += 1
        Category.unique += len(set(self.goods))


