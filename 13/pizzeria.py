import logging

from waiter import Waiter
from menu import Menu
from kitchen import Kitchen

logging.basicConfig(level=logging.DEBUG)


kitchen = Kitchen()
menu = Menu()
w = Waiter(menu=menu, kitchen=kitchen)
w.greet_guest()

logging.info('Restaurant now serving')
while w.serving:
    w.serve_guest()
