from dish import Dish


class Menu(object):

    def __init__(self):
        self.menu = []
        self.menu.append(Dish(dish_name="Margherita"))
        self.menu.append(Dish(dish_name="Napoletana"))
        self.menu.append(Dish(dish_name="Pepperoni"))

    def contents(self):
        return self.menu
