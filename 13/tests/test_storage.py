from storage import Storage
from ingredient import Ingredient


def test_fetch_empty_ingredients_returns_true():
    storage = Storage()
    assert storage.fetch(ingredients=[]) is True


def test_fetch_nonexistent_ingredient_returns_false():
    storage = Storage()
    assert storage.fetch(ingredients=[Ingredient(name='Non existent', amount=8)]) is False


def test_fetch_existent_item_returns_true():
    storage = Storage()
    assert storage.fetch(ingredients=[Ingredient(name=Ingredient.TOMATO, amount=1)]) is True


def test_fetch_multiple_items_should_work():
    storage = Storage()
    ingredients = [
        Ingredient(name=Ingredient.TOMATO, amount=1),
        Ingredient(name=Ingredient.DOUGH, amount=1)
    ]
    assert storage.fetch(ingredients) is True


def test_fetch_too_many_items_returns_false():
    storage = Storage()
    ingredients = [
        Ingredient(name=Ingredient.TOMATO, amount=90),
    ]
    assert storage.fetch(ingredients) is False
