"""OOP deck of playing cards

Deck generates 52 or 54 Card objects (depending on joker=True/False) which
are stored in a list that is ordered by suit and value, but can be shuffled.
As cards are dealt, they are removed from the deck, but number of remaining cards is
tracked.

Example usage:


from deck import Deck

deck = Deck()
deck.shuffle()
card = deck.deal_one()



Executing deck.py creates a deck, shuffles the deck, deals a card, and prints remaining
card count.
"""

# Imports
import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return str(self.value) + " of " + str(self.suit)

    def __repr__(self):
        return str(self.value) + " of " + str(self.suit)


class Deck:

    # Declare suits and values
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    values = [v for v in range(2, 11)]
    values += ['J', 'Q', 'K', 'A']

    def __init__(self, jokers=False):
        self.cards = []
        for suit in self.suits:
            for value in self.values:
                card = Card(suit, value)
                self.cards.append(card)
        if jokers:
            self.cards.append([Card('joker1', 'joker'), Card('joker2', 'joker')])

    def shuffle(self):
        random.shuffle(self.cards)

    def list_all(self):
        for card in self.cards:
            print(card)

    def deal_one(self):
        return self.cards.pop()

    def remaining_cards(self):
        return len(self.cards)


if __name__ == '__main__':
    d = Deck()
    d.shuffle()
    print(d.deal_one())
    print(d.remaining_cards())
