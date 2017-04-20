from ingredient import Ingredient


class Storage:

    def __init__(self):
        self.items = {
            Ingredient.TOMATO: Ingredient(name=Ingredient.TOMATO, amount=8),
            Ingredient.DOUGH: Ingredient(name=Ingredient.DOUGH, amount=2),
            Ingredient.MOZZARELLA: Ingredient(name=Ingredient.MOZZARELLA, amount=1),
            Ingredient.PEPPERONI: Ingredient(name=Ingredient.PEPPERONI, amount=0.3)
        }

    def fetch(self, ingredients):
        all_ingredients_are_there = all([i.name in self.items for i in ingredients])

        if all_ingredients_are_there:
            # List needs to be called to evaluate map here
            list(map(lambda x: self.items[x.name].use(amount=x.amount), ingredients))

            print('STORAGE: Inventory is now...')
            print('\n'.join([f'{i.amount} {i.name}' for i in self.items.values()]))

        return all_ingredients_are_there
