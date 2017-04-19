from ingredient import Ingredient


class Storage(object):

    def __init__(self):
        self.items = {
            Ingredient.TOMATO: Ingredient(name=Ingredient.TOMATO, amount=8),
            Ingredient.DOUGH: Ingredient(name=Ingredient.DOUGH, amount=2),
            Ingredient.MOZZARELLA: Ingredient(name=Ingredient.MOZZARELLA, amount=1),
            Ingredient.PEPPERONI: Ingredient(name=Ingredient.PEPPERONI, amount=0.3)
        }

    def fetch(self, ingredients):
        for ingredient in ingredients:
            storage_item = self.items.get(ingredient.name, None)
            if storage_item:
                storage_item.use(amount=ingredient.amount)
            else:
                return False
        return True
