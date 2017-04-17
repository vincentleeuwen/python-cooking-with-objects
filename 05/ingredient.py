
class Ingredient(object):
    TOMATO = "Tomato"
    DOUGH = "Dough"
    MOZZARELLA = "Mozzarella"
    ANCHOVIES = "Anchovies"
    PEPERONI = "Peperoni"

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
