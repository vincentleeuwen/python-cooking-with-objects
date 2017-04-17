from ingredient import Ingredient


class Storage(object):

    def __init__(self):
        self.items = [
            Ingredient(name=Ingredient.TOMATO, amount=8),
            Ingredient(name=Ingredient.DOUGH, amount=2),
            Ingredient(name=Ingredient.MOZZARELLA, amount=1),
            Ingredient(name=Ingredient.PEPPERONI, amount=0.3),
        ]

    def check_storage(self, ingredient):
        for storage_item in self.items:
            if ingredient.name == storage_item.name:
                return storage_item

    def fetch(self, ingredients):
        for ingredient in ingredients:
            storage_item = self.check_storage(ingredient)
            if storage_item:
                storage_item.use(amount=ingredient.amount)
            else:
                return False
        return True
