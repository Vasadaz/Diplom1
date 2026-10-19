from practicum.bun import Bun

import pytest


class TestBun:
    name = "Бриошь"
    price = 80.0

    def test__init__create_instance__true(self):
        bun = Bun(self.name, self.price)

        assert isinstance(bun, Bun)
        assert bun.name == self.name
        assert bun.price == self.price

    def test__get_name__get_name__true(self):
        bun = Bun(self.name, self.price)

        assert bun.get_name() == self.name

    def test__get_price__get_price__true(self):
        bun = Bun(self.name, self.price)

        assert bun.get_price() == self.price
