import unittest

from services.cards import *


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.card_str = "10D"
        self.card_str_bad = "D10"

    def test_card_from_string(self):
        assert Card(8, 2) == card_from_string(self.card_str)


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card1 = card_from_string("10D")
        self.card2 = card_from_string("10S")
        self.card3 = card_from_string("9D")
        self.card4 = card_from_string("10D")

    def test_equality(self):
        assert self.card1 == self.card2
        assert self.card1 == self.card4
        assert self.card1 != self.card3

    def test_hash(self):
        assert hash(self.card1) != hash(self.card2)
        assert hash(self.card1) == hash(self.card4)

    def test_inequality(self):
        assert self.card1 > self.card3
        assert self.card3 < self.card2
        assert not (self.card4 <= self.card3)
        assert self.card4 >= self.card2


class TestHand(unittest.TestCase):

    def test_init(self):
        pass


if __name__ == '__main__':
    unittest.main()
