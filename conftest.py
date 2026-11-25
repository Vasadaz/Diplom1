"""Общие фикстуры для юнит-тестов Stellar Burgers."""
from unittest.mock import Mock

import pytest

from practicum.bun import Bun
from practicum.burger import Burger
from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

@pytest.fixture
def bun():
    """Вернуть мок булочки с предсказуемыми именем и ценой."""
    mock = Mock()
    mock.get_name.return_value = "Бриошь"
    mock.get_price.return_value = 80
    return mock

@pytest.fixture
def make_ingredient():
    """Вернуть фабрику моков ингредиентов с заданными именем, ценой и типом."""

    def factory(
            name: str = "Котлета",
            price: float = 100,
            ingredient_type: str = INGREDIENT_TYPE_FILLING,
    ) -> Mock:
        """Создать мок ингредиента."""
        mock = Mock(spec=Ingredient)
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        mock.get_type.return_value = ingredient_type
        return mock

    return factory

@pytest.fixture
def burger_with_three(make_ingredient) -> Burger:
    """Собрать бургер с ингредиентами в порядке: Котлета, Соус, Начинка."""
    burger = Burger()
    for name, price, kind in (
            ("Котлета", 100, INGREDIENT_TYPE_FILLING),
            ("Соус", 20, INGREDIENT_TYPE_SAUCE),
            ("Начинка", 200, INGREDIENT_TYPE_FILLING),
    ):
        burger.add_ingredient(make_ingredient(name, price, kind))
    return burger
