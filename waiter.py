
class Waiter(object):

    def __init__(self, menu, kitchen, tab):
        self.menu = menu
        self.kitchen = kitchen
        self.tab = tab

    def greet_guest(self):
        self.serving = True
        print("Good afternoon, what can I do for you?")

    
