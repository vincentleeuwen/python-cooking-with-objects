from ingredient import Ingredient


class Storage(object):

    def __init__(self):
        self.items = {
            Ingredient.TOMATO: Ingredient(name=Ingredient.TOMATO, amount=8),
            Ingredient.DOUGH: Ingredient(name=Ingredient.DOUGH, amount=2),
            Ingredient.MOZZARELLA: Ingredient(name=Ingredient.MOZZARELLA, amount=1),
            Ingredient.PEPPERONI: Ingredient(name=Ingredient.PEPPERONI, amount=0.3)
        }

    # def check_storage(self, ingredient):
    #     for storage_item in self.items:
    #         if ingredient.name == storage_item.name:
    #             return storage_item

    def fetch(self, ingredients):
        checklist = []
        for ingredient in ingredients:
            try:
                # look up the ingredient in the storage
                storage_item = self.items[ingredient.name]
            except KeyError:
                # the ingredient isn't there
                checklist.append(False)
            else:
                # we now know it's there, so we can use the storage_item
                # to check if the available quantity is enough
                checklist.append(storage_item.amount >= ingredient.amount)

        ingredients_are_there = False not in checklist
        if ingredients_are_there:
            for ingredient in ingredients:
                # we can index into our dictionary without precaution now because
                # we know the ingredients are there
                self.items[ingredient.name].use(amount=ingredient.amount)

        return ingredients_are_there
