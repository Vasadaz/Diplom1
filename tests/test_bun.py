from practicum.bun import Bun
from data.test_data import NAME_BUN, PRICE_BUN

import pytest


class TestBun:

    def test__init__create_instance__true(self):
        bun = Bun(NAME_BUN, PRICE_BUN)

        assert isinstance(bun, Bun)
        assert bun.name == NAME_BUN
        assert bun.price == PRICE_BUN

    def test__get_name__get_name__true(self):
        bun = Bun(NAME_BUN, PRICE_BUN)

        assert bun.get_name() == NAME_BUN

    def test__get_price__get_price__true(self):
        bun = Bun(NAME_BUN, PRICE_BUN)

        assert bun.get_price() == PRICE_BUN
