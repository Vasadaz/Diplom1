from practicum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

from data.test_data import TYPE_FILLING, TYPE_SAUCE

import pytest


class TestIngredient:

    @pytest.mark.parametrize(
        ('type', 'type_name'),
        ((INGREDIENT_TYPE_FILLING, TYPE_FILLING), (INGREDIENT_TYPE_SAUCE, TYPE_SAUCE))
    )
    def test__ingredient_type__get_type__true(self, type, type_name):
        assert type == type_name
