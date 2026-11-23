from practicum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

import pytest


class TestIngredient:
    type_filling = 'FILLING'
    type_sauce = 'SAUCE'

    @pytest.mark.parametrize(
        ('type', 'type_name'),
        ((INGREDIENT_TYPE_FILLING, type_filling), (INGREDIENT_TYPE_SAUCE, type_sauce))
    )
    def test__ingredient_type__get_type__true(self, type, type_name):
        assert type == type_name





