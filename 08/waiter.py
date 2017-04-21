from check import Check


class Waiter:

    def __init__(self, menu, kitchen):
        self.menu = menu
        self.kitchen = kitchen
        self.check = Check()
        self.serving = True

    def greet_guest(self):
        print("Good day. Welcome to our lovely little restaurant.")

    def serve_guest(self):
        print("How can I be of service?")
        print("1. Would you like to order a pizza?")
        print("2. Would you like to leave?")

        choice = input()
        self.take_order(order_number=int(choice))

    def take_order(self, order_number):
        if order_number == 1:
            print("Let me get the menu")
            self.list_menu()
            self.order_food(choice=int(input()))
        elif order_number == 2:
            print("Thank you for your visit!")
            self.serving = False
        else:
            print("I really don't understand")

    def list_menu(self):
        for index, dish in enumerate(self.menu.contents()):
            print(index, dish.name)

    def order_food(self, choice):
        chosen_dish = self.menu.contents()[choice]
        if self.kitchen.order(dish=chosen_dish):
            print("Dish is on the way")
            self.check.add(item=chosen_dish)
        else:
            print("Sorry, this dish is not available")
