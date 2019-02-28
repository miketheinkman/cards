"""Simple 'War' implementation

Based on OOP deck of playing cards.

Usage: python3 war.py
"""

# Imports
from .deck import Deck

# Create and shuffle deck
deck = Deck()
deck.shuffle()

# Create lists for hands and cards in play
player = []
bot = []
war = []


# Deal entire deck
while deck.cards:
    player.append(deck.deal_one())
    bot.append(deck.deal_one())


# Assign integer values to face cards
def eval_card(card):
    values = {'J': 11, 'Q': 12, 'K': 13, 'A': 14, }
    if str(card.value) in 'JQKA':
        return values[card.value]
    else:
        return card.value


# Eval each hand for winner
def play_hand(pl_c=None, bot_c=None):
    if eval_card(pl_c) == eval_card(bot_c) and pl_c and bot_c:
        return "war"
    elif eval_card(pl_c) > eval_card(bot_c):
        return "player"
    else:
        return "bot"


# When IndexError caught eval winner
def check_winner(player=player, bot=bot):
    if player and not bot:
        for _ in range(10):
            buffered_print('You Win!!!!!!!!!!!!!!!')
        return True

    elif bot and not player:
        for _ in range(10):
            buffered_print('Computer wins :-( :-(')
        return True


# Minimize print for styling
def buffered_print(s):
    print()
    print(s)
    print()


# Game loop
while True:

    # Play 'em if ya got 'em
    try:
        p_card = player.pop()
        b_card = bot.pop()

    # If ya don't got 'em, somebody wins
    except IndexError:

        # verify winner, declare winner, break loop
        if check_winner():
            break

    # Add played cards to war chest
    war = war + [p_card, b_card]

    # Print general info
    print("Player: {0} cards -- Computer: {1} cards -- War: {2} cards -- "
          "Total: {3} cards".format(
                                    len(player),
                                    len(bot),
                                    len(war),
                                    len(player) + len(bot) + len(war)
                                    ))
    print("--------------------------------------------------------------")
    buffered_print("Computer played {}. Press Enter to continue.".format(b_card))

    # input used for loop control
    input()
    buffered_print("You played {}".format(p_card))

    # eval cards in play
    try:

        # if cards in play are equal
        if play_hand(pl_c=p_card, bot_c=b_card) == "war":

            # add additional 'face down' cards to war chest and declare war
            war = war + [player.pop(), bot.pop()]
            buffered_print("It's War!!")

        # if player has higher card
        elif play_hand(pl_c=p_card, bot_c=b_card) == "player":

            # declare them the winner
            buffered_print("You win this hand")

            # insert war chest cards onto the 'bottom' of the player deck
            for card in war:
                player.insert(0, card)

            # empty war chest
            war = []

        # if bot has higher card
        elif play_hand(pl_c=p_card, bot_c=b_card) == "bot":

            # declare them the winner
            buffered_print("Computer wins this hand")

            # insert war chest cards onto the 'bottom' of the bot deck
            for card in war:
                bot.insert(0, card)

            # empty war chest
            war = []

    # if a player is out of cards
    except IndexError:

        # verify a win, declare the winner and break loop
        if check_winner():
            break
