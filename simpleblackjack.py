"""  Simple single player/single hand blackjack game

Based on OOP deck of playing cards.

Usage: python3 simpleblackjack.py
"""

# Imports
from deck import Deck
import os


# Find total value of all cards in hand
def evaluate_hand(hand):
    non_aces = [c.value for c in hand if c.value != 'A']
    aces = [c.value for c in hand if c.value == 'A']
    total = 0
    for card in non_aces:
        if str(card) in 'JQK':
            total += 10
        else:
            total += int(card)

    for _ in aces:
        if total <= 10:
            total += 11
        else:
            total += 1
    return total

# Create and shuffle deck
deck = Deck()
deck.shuffle()

# Initialize lists for hands
player = []
dealer = []

# Initial Deal
player.append(deck.deal_one())
dealer.append(deck.deal_one())
player.append(deck.deal_one())
dealer.append(deck.deal_one())

# Game Loop
standing = False
first = True
while True:

    # Clear term on loop
    os.system('cls' if os.name == 'nt' else 'clear')

    # Eval 'natural' blackjack
    if evaluate_hand(player) == 21 and first:
        print("Blackjack!")
        print()
        break

    # Eval player bust
    if evaluate_hand(player) > 21:
        print("You busted. Better luck next time.")
        print()
        break

    # Stand logic
    if standing:

        # Dealer hits
        while evaluate_hand(dealer) < 18:
            dealer.append(deck.deal_one())

        # Print info
        print("Dealer has {}".format(', '.join([c.__str__() for c in dealer])))
        print("Dealer has {}".format(evaluate_hand(dealer)))
        print()
        print("Player has {}".format(', '.join([c.__str__() for c in player])))
        print("Player has {}".format(evaluate_hand(player)))
        print()

        # Eval dealer bust
        if evaluate_hand(dealer) > 21:
            print("Dealer busted. You Win!!")
            print()
            break

        # Eval push
        elif evaluate_hand(dealer) == evaluate_hand(player):
            print("Push. Nobody wins.")
            print()
            break

        # Eval dealer win
        elif evaluate_hand(dealer) > evaluate_hand(player):
            print("Dealer wins.")
            print()
            break

        # Player win by elimination of other options
        else:
            print("You win!!")
            print()
            break

    # Pre stand logic
    else:

        # Show only dealer face up card
        print("Dealer showing: " + dealer[0].__str__())
        print()

    # Show player hand
    print("Player has {}".format(', '.join([c.__str__() for c in player])))
    print("Total value: {}".format(evaluate_hand(player)))
    print()
    print()

    # Hit/stand logic
    action = input("1 to hit, or 2 to stand. \n")
    if action == "1":
        first = False
        player.append(deck.deal_one())
    elif action == "2":
        standing = True
