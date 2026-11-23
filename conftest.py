"""Общие фикстуры для юнит-тестов Stellar Burgers."""
from unittest.mock import Mock

import pytest

from practicum.bun import Bun
from practicum.ingredient import Ingredient
from practicum.ingredient_types import INGREDIENT_TYPE_FILLING

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