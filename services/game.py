

SUITS = ["S", "D", "H", "C"]
RANKS = range(1, 14)
DECK = [(suit, rank) for rank in RANKS for suit in SUITS]

class Game:

    def __init__(self):
        self.board = []

    def reset(self):
        self.board = []

    def update(self, cards):
        if len(self.board) + len(cards) > 7:
            self.reset()
        for card_val in cards:
            card = self._interpret(card_val)
            if card != None:
                self.board += [card]

    def _interpret(self, val):
        card = (val[0], val[1])
        if card[0] in DECK:
            return card
        return None

    def get_odds(self):
        print(self.pair_odds)

    def pair_odds(self):


