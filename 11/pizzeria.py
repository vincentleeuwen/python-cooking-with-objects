from waiter import Waiter
from menu import Menu
from kitchen import Kitchen

kitchen = Kitchen()
menu = Menu()
w = Waiter(menu=menu, kitchen=kitchen)
w.greet_guest()
while w.serving:
    w.serve_guest()
