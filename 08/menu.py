from dish import Dish
from ingredient import Ingredient


class Menu:

    def __init__(self):
        self.menu = []
        self.menu.append(Dish(
            dish_name="Margherita",
            ingredients=[
                Ingredient(name=Ingredient.TOMATO, amount=3),
                Ingredient(name=Ingredient.DOUGH, amount=0.25),
                Ingredient(name=Ingredient.MOZZARELLA, amount=0.2)
            ])
        )
        self.menu.append(Dish(
            dish_name="Napoletana",
            ingredients=[
                Ingredient(name=Ingredient.TOMATO, amount=3),
                Ingredient(name=Ingredient.DOUGH, amount=0.25),
                Ingredient(name=Ingredient.MOZZARELLA, amount=0.2),
                Ingredient(name=Ingredient.ANCHOVIES, amount=0.05)
            ])
        )
        self.menu.append(Dish(
            dish_name="Pepperoni",
            ingredients=[
                Ingredient(name=Ingredient.TOMATO, amount=3),
                Ingredient(name=Ingredient.DOUGH, amount=0.25),
                Ingredient(name=Ingredient.MOZZARELLA, amount=0.2),
                Ingredient(name=Ingredient.PEPPERONI, amount=0.1)
            ])
        )

    def contents(self):
        return self.menu
