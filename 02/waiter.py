
class Waiter(object):

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
            answer = "Let me get the menu"
        elif order_number == 2:
            answer = "Thank you for your visit!"
        else:
            answer = "I really don't understand"
        print(answer)
