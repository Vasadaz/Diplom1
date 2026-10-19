from practicum.bun import Bun
from practicum.burger import Burger
from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

import pytest


class TestBurger:
    # Булочка
    name_bun = 'Бриошь'
    price_bun = 80

    # Начинка
    name_filling = 'Котлета'
    price_filling = 100

    # Соус
    name_sauce = 'Кетчуп'
    price_sauce = 20

    def test__init__create_instance__true(self):
        burger = Burger()

        assert isinstance(burger, Burger)
        assert burger.bun is None
        assert burger.ingredients == []

    def test__set_buns__set_buns__true(self):
        bun = Bun(self.name_bun, self.price_bun)

        burger = Burger()
        burger.set_buns(bun)

        assert burger.bun is bun

    def test__add_ingredient__add_ingredient__true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, self.name_filling, self.price_filling)

        burger = Burger()
        burger.add_ingredient(ingredient)

        assert burger.ingredients == [ingredient]

    def test__remove_ingredient__remove_ingredient__true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, self.name_filling, self.price_filling)

        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test__move_ingredient__move_ingredient__true(self):
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, self.name_filling, self.price_filling)
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, self.name_sauce, self.price_sauce)

        burger = Burger()
        burger.add_ingredient(ingredient_filling)
        burger.add_ingredient(ingredient_sauce)
        burger.move_ingredient(1, 0)

        assert burger.ingredients == [ingredient_sauce, ingredient_filling]

    def test__get_price__get_price__true(self):
        bun = Bun(self.name_bun, self.price_bun)
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, self.name_filling, self.price_filling)
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, self.name_sauce, self.price_sauce)

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_filling)
        burger.add_ingredient(ingredient_sauce)

        assert burger.get_price() == self.price_bun * 2 + self.price_filling + self.price_sauce

    def test__get_receipt__get_receipt__true(self):
        bun = Bun(self.name_bun, self.price_bun)
        ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, self.name_filling, self.price_filling)
        ingredient_sauce = Ingredient(INGREDIENT_TYPE_SAUCE, self.name_sauce, self.price_sauce)

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient_filling)
        burger.add_ingredient(ingredient_sauce)

        receipt = [
            f'(==== {self.name_bun} ====)',
            f'= {ingredient_filling.type.lower()} {self.name_filling} =',
            f'= {ingredient_sauce.type.lower()} {self.name_sauce} =',
            f'(==== {self.name_bun} ====)\n',
            f'Price: {self.price_bun * 2 + self.price_filling + self.price_sauce}',
        ]

        assert burger.get_receipt() == '\n'.join(receipt)



