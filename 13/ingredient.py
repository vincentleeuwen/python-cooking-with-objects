import logging


class Ingredient:
    TOMATO = "Tomato"
    DOUGH = "Dough"
    MOZZARELLA = "Mozzarella"
    ANCHOVIES = "Anchovies"
    PEPPERONI = "Pepperoni"

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def use(self, amount):
        self.amount -= amount
        logging.debug('Used %s %s', self.amount, self.name)
