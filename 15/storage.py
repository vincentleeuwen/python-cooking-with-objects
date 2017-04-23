from ingredient import Ingredient


class Storage:
    """Storage for ingredients used by Pizzeria

    This class holds all ingredients available to create pizza's in our restaurant.
    On creation the Storage starts with a fixed set of Ingredients:

        8 Tomato
        2 Dough
        1 Mozzarella
        0.3 Pepperoni

    Attributes:
        items (:obj:`dict` with :obj:Ingredient): Ingredients available in this storage
    """
    def __init__(self):
        self.items = {
            Ingredient.TOMATO: Ingredient(name=Ingredient.TOMATO, amount=8),
            Ingredient.DOUGH: Ingredient(name=Ingredient.DOUGH, amount=2),
            Ingredient.MOZZARELLA: Ingredient(name=Ingredient.MOZZARELLA, amount=1),
            Ingredient.PEPPERONI: Ingredient(name=Ingredient.PEPPERONI, amount=0.3)
        }

    def fetch(self, ingredients):
        """Fetch items from storage

        This method checks to see whether the enough required Ingredients are present in
        the Storage and updates the amounts accordingly.

        Args:
            items (:obj:`list` of :obj:Ingredient): Items to be fetched

        Returns:
            True if successful, False otherwise.
        """
        # Check whether all required ingredients exist in storage and we have enough of them
        all_ingredients_are_there = all(
            [i.name in self.items and self.items[i.name].amount >= i.amount for i in ingredients])

        if all_ingredients_are_there:
            # List needs to be called to evaluate map here
            list(map(lambda x: self.items[x.name].use(amount=x.amount), ingredients))

            print('STORAGE: Inventory is now...')
            print('\n'.join([f'{i.amount} {i.name}' for i in self.items.values()]))

        return all_ingredients_are_there
