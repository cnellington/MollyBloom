from services.cards import *


card1 = card_from_string('10S')
card2 = card_from_string('AD')

print(card1)
print(card2)

hand = Hand([card1]*5)
print(hand)
print(card1 < card2)
