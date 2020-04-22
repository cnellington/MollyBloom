
###################
# Constants #######
###################
RANK_STR = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUIT_STR = ['C', 'H', 'D', 'S']
RANK = {}
RANK_REV = {}
for i in range(len(RANK_STR)):
    RANK[RANK_STR[i]] = i
    RANK_REV[i] = RANK_STR[i]
SUIT = {}
SUIT_REV = {}
for i in range(len(SUIT_STR)):
    SUIT[SUIT_STR[i]] = i
    SUIT_REV[i] = SUIT_STR[i]


###################
# Exposed Classes #
###################
class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{RANK_REV[self.rank]} of {SUIT_REV[self.suit]}"

    def __hash__(self):
        return hash((self.rank, self.suit))

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return (self < other) or (self == other)

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)


class Hand:

    def __init__(self, cards):
        self.cards = cards
        self.cards.sort()

    def __str__(self):
        ret = ""
        for card in self.cards:
            ret += str(card) + ", "
        ret = ret[:-2]
        return ret

    def __hash__(self):
        return NotImplemented

    def __eq__(self, other):
        return NotImplemented

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return NotImplemented

    def __le__(self, other):
        return (self < other) or (self == other)

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)


###################
# Exposed Utils ###
###################
def card_from_string(card_str):
    suit = card_str[-1:]
    rank = card_str[:-1]
    card = Card(RANK[rank], SUIT[suit])
    return card
