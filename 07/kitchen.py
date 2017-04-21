from storage import Storage


class Kitchen:

    def __init__(self):
        self.storage = Storage()

    def order(self, dish):
        print("KITCHEN: Order received for {0}".format(dish.name))
        print("I'm gonna need some:")

        for ingredient in dish.ingredients:
            print("{0} - {1}".format(ingredient.amount, ingredient.name))

        return self.storage.fetch(ingredients=dish.ingredients)
