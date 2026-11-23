"""Юнит-тесты класса Burger. Внешние сущности замокированы."""
from unittest.mock import Mock

import pytest

from practicum.bun import Bun
from practicum.burger import Burger
from practicum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


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


class TestBurgerStructure:
    """Инициализация, установка булочки, состав ингредиентов."""

    def test_init_creates_empty_burger(self):
        """Новый бургер пуст: булочки нет, список ингредиентов пустой."""
        burger = Burger()

        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns_stores_bun(self, bun):
        """Установленная булочка сохраняется в атрибуте bun."""
        burger = Burger()
        burger.set_buns(bun)

        assert burger.bun is bun

    def test_set_buns_replaces_previous_bun(self, bun):
        """Повторный вызов set_buns заменяет ранее установленную булочку."""
        other_bun = Mock(spec=Bun)
        burger = Burger()

        burger.set_buns(bun)
        burger.set_buns(other_bun)

        assert burger.bun is other_bun

    def test_add_ingredient_appends_to_end(self, make_ingredient):
        """Новый ингредиент добавляется в конец списка, старые не смещаются."""
        burger = Burger()
        first = make_ingredient("Котлета", 100)
        second = make_ingredient("Соус", 20, INGREDIENT_TYPE_SAUCE)

        burger.add_ingredient(first)
        burger.add_ingredient(second)

        assert burger.ingredients == [first, second]

    @pytest.mark.parametrize(
        ("index", "expected_names"),
        [
            (0, ["Соус", "Начинка"]),
            (1, ["Котлета", "Начинка"]),
            (-1, ["Котлета", "Соус"]),
        ],
    )
    def test_remove_ingredient_removes_only_target(
            self, burger_with_three, index, expected_names
    ):
        """Удаляется только ингредиент по индексу, остальные и порядок сохранены."""
        burger_with_three.remove_ingredient(index)

        assert [item.get_name() for item in burger_with_three.ingredients] == expected_names

    def test_remove_ingredient_empty_list_raises(self):
        """Удаление из пустого бургера приводит к IndexError."""
        with pytest.raises(IndexError):
            Burger().remove_ingredient(0)

    def test_remove_ingredient_out_of_range_raises(self, burger_with_three):
        """Индекс за границей списка приводит к IndexError."""
        with pytest.raises(IndexError):
            burger_with_three.remove_ingredient(5)

    @pytest.mark.parametrize(
        ("old_index", "new_index", "expected_names"),
        [
            (1, 0, ["Соус", "Котлета", "Начинка"]),
            (0, 2, ["Соус", "Начинка", "Котлета"]),
            (2, 0, ["Начинка", "Котлета", "Соус"]),
            (1, 1, ["Котлета", "Соус", "Начинка"]),
        ],
    )
    def test_move_ingredient_reorders(
            self, burger_with_three, old_index, new_index, expected_names
    ):
        """Ингредиент переносится на новую позицию, остальные смещаются."""
        burger_with_three.move_ingredient(old_index, new_index)

        assert [item.get_name() for item in burger_with_three.ingredients] == expected_names

    def test_move_ingredient_keeps_length(self, burger_with_three):
        """Перемещение не меняет количество ингредиентов."""
        burger_with_three.move_ingredient(0, 2)

        assert len(burger_with_three.ingredients) == 3

    def test_move_ingredient_out_of_range_raises(self, burger_with_three):
        """Несуществующий индекс источника приводит к IndexError."""
        with pytest.raises(IndexError):
            burger_with_three.move_ingredient(10, 0)
        # TODO: проверить, потому что семантика отрицательного new_index
        # (insert(-1, ...)) в ТЗ не описана — сейчас это «перед последним».


class TestBurgerPrice:
    """Расчёт стоимости бургера."""

    @pytest.mark.parametrize(
        ("bun_price", "ingredient_prices", "expected"),
        [
            (80, [], 160),
            (0, [], 0),
            (80, [100], 260),
            (80, [100, 20], 280),
            (99.5, [0.5], 199.5),
        ],
    )
    def test_get_price_sums_double_bun_and_ingredients(
            self, bun, make_ingredient, bun_price, ingredient_prices, expected
    ):
        """Цена = цена булочки * 2 + сумма цен всех ингредиентов."""
        bun.get_price.return_value = bun_price
        burger = Burger()
        burger.set_buns(bun)

        for price in ingredient_prices:
            burger.add_ingredient(make_ingredient(price=price))

        assert burger.get_price() == expected

    def test_get_price_requests_bun_price_once(self, bun):
        """Цена булочки запрашивается ровно один раз (для двух половинок)."""
        burger = Burger()
        burger.set_buns(bun)

        burger.get_price()

        bun.get_price.assert_called_once_with()

    def test_get_price_without_bun_raises(self):
        """Без установленной булочки расчёт цены падает с AttributeError."""
        with pytest.raises(AttributeError):
            Burger().get_price()


class TestBurgerReceipt:
    """Формирование чека."""

    def test_get_receipt_with_ingredients(self, bun, make_ingredient):
        """Чек содержит булочку сверху и снизу, ингредиенты в нижнем регистре и цену."""
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(make_ingredient("Котлета", 100, INGREDIENT_TYPE_FILLING))
        burger.add_ingredient(make_ingredient("Кетчуп", 20, INGREDIENT_TYPE_SAUCE))

        expected = "\n".join([
            "(==== Бриошь ====)",
            "= filling Котлета =",
            "= sauce Кетчуп =",
            "(==== Бриошь ====)\n",
            "Price: 280",
        ])

        assert burger.get_receipt() == expected

    def test_get_receipt_without_ingredients(self, bun):
        """Пустой бургер печатает только две булочки и цену; перед Price — пустая строка."""
        burger = Burger()
        burger.set_buns(bun)

        expected = "(==== Бриошь ====)\n(==== Бриошь ====)\n\nPrice: 160"

        assert burger.get_receipt() == expected
