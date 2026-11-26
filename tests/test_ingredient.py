from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

from data.test_data import NAME_FILLING, PRICE_FILLING

import pytest


class TestIngredient:

    def test__init__create_instance__true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, NAME_FILLING, PRICE_FILLING)

        assert isinstance(ingredient, Ingredient)

    def test__get_price__get_price__true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, NAME_FILLING, PRICE_FILLING)

        assert ingredient.get_price() == PRICE_FILLING

    def test__get_name__get_name__true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, NAME_FILLING, PRICE_FILLING)

        assert ingredient.get_name() == NAME_FILLING

    def test__get_type__get_type__true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, NAME_FILLING, PRICE_FILLING)

        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING
