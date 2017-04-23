from check import Check
from dish import Dish


def test_calculate_sum():
    pasta = Dish('Pasta', [], 10)
    pizza = Dish('Pizza', [], 15)
    c = Check()

    # Without any items check sum must be 0
    assert c.calculate_sum() == 0

    # Adding an item should have sum equal to the item
    c.add(pasta)
    assert c.calculate_sum() == 10

    # Adding another item should have sum equal sum of both items
    c.add(pizza)
    assert c.calculate_sum() == 25
