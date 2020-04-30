from itertools import combinations
import random

from services.cards import *

DECK = set([RANK_STR[i]+SUIT_STR[j] for j in range(len(SUIT_STR)) for i in range(len(RANK_STR))])

class Game:

    def __init__(self):
        self.hand = set()
        self.board = set()
        self.deck = DECK

    def update(self, cards):
        if len(self.hand) + len(self.board) >= 7:
            self.hand = set()
            self.board = set()
            self.deck = DECK
        if len(self.deck.intersection(cards)) != len(cards):
            raise ValueError("Invalid card or card is already being used")

        # Update hand, board, and deck
        if not self.hand:
            self.hand = self.hand.union(cards)
        else:
            self.board = self.board.union(cards)
        self.deck = self.deck - self.hand - self.board

    def get_winning_odds(self):
        # TODO: scale probability with number of players
        total = 0
        win_count = 0
        best_hand = None
        for n in range(1000):
            opp_cards = random.sample(list(self.deck), k=2)
            board_cards = random.sample(list(self.deck-set(opp_cards)), k=(5-len(self.board)))
            board = list(self.board) + board_cards
            my_cards = list(self.hand)
            opp_hand = self._best_hand(opp_cards+board)
            my_hand = self._best_hand(my_cards+board)
            if best_hand is None or my_hand > best_hand:
                best_hand = my_hand
            win_count += int(my_hand > opp_hand)
            total += 1
        return (win_count / total), best_hand

    def _best_hand(self, cards):
        hands = list(combinations(cards, 5))
        best_hand = hand_from_list(hands[0])
        for hand_cards in hands:
            hand = hand_from_list(hand_cards)
            if hand > best_hand:
                best_hand = hand
        return best_hand

    def __str__(self):
        return f"{self.board}\n{self.hand}\n{len(self.deck)} cards unused/unknown"
