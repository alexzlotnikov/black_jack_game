import itertools
from random import shuffle

# Initial lists of values
suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
suits_symbols = ['♠', '♦', '♥', '♣']
name_symbol = {'Spades': '♠', 'Diamonds': '♦', 'Hearts': '♥', 'Clubs': '♣'}
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
ranks_symbol = {'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5', 'Six': '6', 'Seven': '7', 'Eight': '8',
                'Nine': '9', 'Ten': '10', 'Jack': 'J', 'Queen': 'Q', 'King': 'K', 'Ace': 'A'}
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 1}


# Define class for Card object
class Card:

    # Create Card objects with suit and rank
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    # Return Card value
    def __str__(self):
        return f'{ranks_symbol[self.rank]} of {name_symbol[self.suit]}'

    # print a card
    def show_face(self):
        card_face = []
        card_face.append("┌─────────┐")
        card_face.append(f"│{ranks_symbol[self.rank]}. . . . │")
        card_face.append("│. . . . .│")
        card_face.append(f"│. . {name_symbol[self.suit]} . .│")
        card_face.append("│. . . . .│")
        card_face.append(f"│. . . .{ranks_symbol[self.rank]} │")
        card_face.append("└─────────┘")
        return card_face

    # Print card back
    def show_back(self):
        card_back = []
        card_back.append("┌─────────┐")
        card_back.append("│# # # # #│")
        card_back.append("│# # # # #│")
        card_back.append("│# # # # #│")
        card_back.append("│# # # # #│")
        card_back.append("│# # # # #│")
        card_back.append("└─────────┘")
        return card_back


# Create class of gaming deck with 52 cards.
class Deck:

    # Create a new deck and shuffle it
    def __init__(self):
        self.all_cards = [Card(suit, rank) for suit, rank in itertools.product(suits, ranks)]

        self.deck_of_cards = self.all_cards
        shuffle(self.deck_of_cards)

    def deck_shuffle(self):
        self.deck_of_cards = self.all_cards
        shuffle(self.deck_of_cards)

    # Deal one card from a shuffled deck
    def deal_one(self):
        return self.deck_of_cards.pop()
