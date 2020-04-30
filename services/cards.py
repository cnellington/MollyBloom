
###################
# Constants #######
###################
RANK_STR = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
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

    def __hash__(self):
        return hash((self.rank, self.suit))

    def __str__(self):
        return f"{RANK_REV[self.rank]}{SUIT_REV[self.suit]}"

    def __repr__(self):
        return str(self)

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
        if len(cards) != 5:
            raise ValueError("Hands must have 5 cards")
        self.cards = cards

    def __str__(self):
        ret = ""
        for card in self.cards:
            ret += str(card) + ", "
        ret = ret[:-2]
        return ret

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        for card in self.cards:
            if card not in other.cards:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.get_score() < other.get_score()

    def __le__(self, other):
        return (self < other) or (self == other)

    def __gt__(self, other):
        return not (self <= other)

    def __ge__(self, other):
        return not (self < other)

    def get_score(self):
        # Score depends on rank counts
        rank_counts = {card.rank: self.cards.count(card) for card in self.cards}.items()
        score, ranks = zip(*sorted((count, rank) for rank, count in rank_counts)[::-1])
        # Accurate scores for pair(2,1,) two pair(2,2,) trips(3,1,) full house(3,2) and 4-of-a-kind(4,1).
        # Now, get scores for straight(3,1,1,1) flush(3,1,1,2) straight-flush(5,) and no-pair (1,)
        if len(score) == 5:
            # Adjust for 5-high straight
            if ranks[0:2] == (12, 3): ranks = (3, 2, 1, 0, -1)
            straight = (ranks[0] - ranks[4] == 4)
            flush = (len({card.suit for card in self.cards}) == 1)
            score = [[(1,), (3,1,1,1)], [(3,1,1,2), (5,)]][flush][straight]
        return score, ranks


###################
# Exposed Utils ###
###################
def card_from_string(card_str):
    suit = card_str[-1:]
    rank = card_str[:-1]
    card = Card(RANK[rank], SUIT[suit])
    return card


def hand_from_list(card_str_list):
    if len(card_str_list) != 5:
        print(card_str_list)
    return Hand([card_from_string(card_str) for card_str in card_str_list])
