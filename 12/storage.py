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
        checklist = []
        for ingredient in ingredients:
            try:
                # look up the ingredient in the storage
                self.items[ingredient.name]
            except KeyError:
                # the ingredient isn't there, append False
                checklist.append(False)
            else:
                # its there, so append True to our checklist
                checklist.append(True)

        all_ingredients_are_there = False not in checklist
        if all_ingredients_are_there:
            for ingredient in ingredients:
                # we can index into our dictionary without precaution now because
                # we know the ingredients are there
                self.items[ingredient.name].use(amount=ingredient.amount)

            # print an overview of our inventory, so we can keep track
            print("STORAGE: Inventory is now...")
            for ingredient in self.items.values():
                print(ingredient.amount, ingredient.name)

        return all_ingredients_are_there
