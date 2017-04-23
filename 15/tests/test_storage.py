import pytest

from storage import Storage
from ingredient import Ingredient


@pytest.mark.parametrize('ingredients, expected', [
    [[], True],
    [[Ingredient(name='Non existent', amount=8)], False],
    [[Ingredient(name=Ingredient.TOMATO, amount=1)], True],
    [[Ingredient(name=Ingredient.TOMATO, amount=1),
      Ingredient(name=Ingredient.DOUGH, amount=1)], True],
    [[Ingredient(name=Ingredient.TOMATO, amount=90)], False],
])
def test_fetch(ingredients, expected):
    storage = Storage()
    assert storage.fetch(ingredients) == expected
