from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

import pytest


class TestIngredient:
    # Начинка
    name_filling = 'Котлета'
    price_filling = 100

    # Соус
    name_sauce = 'Кетчуп'
    price_sauce = 20

    def test__init__create_instance__true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, self.name_filling, self.price_filling)

        assert isinstance(ingredient, Ingredient)

    def test__get_price__get_price__true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, self.name_filling, self.price_filling)

        assert ingredient.get_price() == self.price_filling

    def test__get_name__get_name__true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, self.name_filling, self.price_filling)

        assert ingredient.get_name() == self.name_filling

    def test__get_type__get_type__true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, self.name_filling, self.price_filling)

        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING





