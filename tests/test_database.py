"""Юнит-тесты класса Database."""
import pytest

from practicum.bun import Bun
from practicum.database import Database
from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestDatabase:
    """Проверка предзаполненного каталога булочек и ингредиентов."""

    @pytest.mark.parametrize(
        ("index", "name", "price"),
        [(0, "black bun", 100), (1, "white bun", 200), (2, "red bun", 300)],
    )
    def test_available_buns_contains_expected_bun(self, index, name, price):
        """По каждому индексу лежит нужная булочка с нужной ценой."""
        buns = Database().available_buns()

        assert isinstance(buns[index], Bun)
        assert buns[index].get_name() == name
        assert buns[index].get_price() == price

    def test_available_buns_returns_exactly_three(self):
        """Каталог содержит ровно три булочки в заданном порядке."""
        names = [bun.get_name() for bun in Database().available_buns()]

        assert names == ["black bun", "white bun", "red bun"]

    @pytest.mark.parametrize(
        ("ingredient_type", "expected_names", "expected_prices"),
        [
            (INGREDIENT_TYPE_SAUCE, ["hot sauce", "sour cream", "chili sauce"], [100, 200, 300]),
            (INGREDIENT_TYPE_FILLING, ["cutlet", "dinosaur", "sausage"], [100, 200, 300]),
        ],
    )
    def test_available_ingredients_grouped_by_type(
        self, ingredient_type, expected_names, expected_prices
    ):
        """Ингредиенты каждого типа присутствуют в каталоге с верными ценами."""
        ingredients = Database().available_ingredients()
        filtered = [item for item in ingredients if item.get_type() == ingredient_type]

        assert all(isinstance(item, Ingredient) for item in ingredients)
        assert [item.get_name() for item in filtered] == expected_names
        assert [item.get_price() for item in filtered] == expected_prices

    def test_available_ingredients_returns_six_items(self):
        """В каталоге шесть ингредиентов: три соуса и три начинки."""
        ingredients = Database().available_ingredients()

        assert len(ingredients) == 6

    def test_instances_do_not_share_storage(self):
        """Каталоги двух экземпляров независимы: правка одного не влияет на другой."""
        first, second = Database(), Database()

        first.available_buns().clear()

        assert len(second.available_buns()) == 3
