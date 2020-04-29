import unittest

from services.cards import *


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.card_str = "TD"
        self.card_str_bad = "DT"

    def test_card_from_string(self):
        assert Card(8, 2) == card_from_string(self.card_str)


class TestCard(unittest.TestCase):

    def setUp(self):
        self.card1 = card_from_string("TD")
        self.card2 = card_from_string("TS")
        self.card3 = card_from_string("9D")
        self.card4 = card_from_string("TD")

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

    def setUp(self):
        self.pair1 = Hand([Card(4,3), Card(4,2), Card(11,0), Card(0,0), Card(12,1)])
        self.pair2 = Hand([Card(4,2), Card(12,1), Card(11,0), Card(4,0), Card(0,0)])
        self.twopair = Hand([Card(4, 2), Card(12, 1), Card(11, 0), Card(4, 3), Card(12, 0)])
        self.trips = Hand([Card(0, 1), Card(0, 0), Card(0, 3), Card(9, 0), Card(11, 0)])
        self.straight = Hand([Card(0,1), Card(1,1), Card(2,2), Card(3,1), Card(4,1)])
        self.flush = Hand([Card(0, 1), Card(5, 1), Card(10, 1), Card(3, 1), Card(4, 1)])
        self.fullhouse = Hand([Card(0, 1), Card(0, 3), Card(5, 1), Card(5, 2), Card(0, 0)])
        self.fours = Hand([Card(0, 1), Card(0, 2), Card(0, 3), Card(0, 0), Card(11, 0)])
        self.sf = Hand([Card(0, 1), Card(1, 1), Card(2, 1), Card(3, 1), Card(4, 1)])

    def test_get_score(self):
        assert self.pair1.get_score()       == ((2, 1, 1, 1), (4, 12, 11, 0))
        assert self.pair2.get_score()       == ((2, 1, 1, 1), (4, 12, 11, 0))
        assert self.twopair.get_score()     == ((2, 2, 1), (12, 4, 11))
        assert self.trips.get_score()       == ((3, 1, 1), (0, 11, 9))
        assert self.straight.get_score()    == ((3, 1, 1, 1), (4, 3, 2, 1, 0))
        assert self.flush.get_score()       == ((3, 1, 1, 2), (10, 5, 4, 3, 0))
        assert self.fullhouse.get_score()   == ((3, 2), (0, 5))
        assert self.fours.get_score()       == ((4, 1), (0, 11))
        assert self.sf.get_score()          == ((5,), (4, 3, 2, 1, 0))

    def test_inequality(self):
        assert self.pair1 == self.pair2  # Test eq
        assert self.pair2 <= self.pair1  # Test le =
        assert self.pair1 <= self.twopair  # Test le <
        assert self.pair1 != self.twopair  # Test ne
        assert self.pair2 < self.twopair  # Test lt
        assert self.twopair < self.trips
        assert self.straight > self.trips  # Test gt
        assert self.flush >= self.straight # Test ge
        assert self.flush < self.fullhouse
        assert self.fullhouse < self.fours
        assert self.fours < self.sf
        assert not (self.sf < self.pair1)


if __name__ == '__main__':
    unittest.main()
