from waiter import Waiter
from menu import Menu

menu = Menu()
w = Waiter(menu=menu)
w.greet_guest()
w.serve_guest()
