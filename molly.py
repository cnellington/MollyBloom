from services.cards import *
from services.game import Game


def main():
    print("Molly Bloom, Poker Odds Calculator")
    print("type quit to exit")
    game = Game()
    entry = ""
    while True:
        entry = input("\nNext cards: ").upper()
        if 'quit' in entry:
            break
        cards = entry.split()
        try:
            game.update(cards)
        except ValueError:
            print("Bad entry, try again")
        print("Game State")
        print(game)
        odds, best_hand = game.get_winning_odds()
        print(f"Winning odds: {odds}")
        print(f"Best possible hand: {best_hand}")
    exit(0)


if __name__ == '__main__':
    main()
