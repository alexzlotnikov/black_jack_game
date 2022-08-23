from time import sleep
import keyboard


# Create class for Player
class Player:

    # Create a player with name, empty hand and started deposit
    def __init__(self, name='Player'):
        self.name = name
        self.hand = []
        self.deposit = 100

    # Deal first two cards to player's hand
    def add_two(self, new_card1, new_card2):
        self.hand.append(new_card1)
        self.hand.append(new_card2)

    # Deal a card to player
    def add_card(self, new_card):
        self.hand.append(new_card)

    # Count player's hand points
    def hand_sum(self):
        hand_values = [card.value for card in self.hand]
        if 1 in hand_values and sum(hand_values) <= 11:
            return sum(hand_values) + 10
        else:
            return sum(hand_values)

    # Printing cards in player's hand
    def show_hand(self):
        cards_in_row = zip(*(c.show_face() for c in self.hand))  # merge cards in hand by the rows
        print('\n'.join(map('  '.join, cards_in_row)))  # printing cards in hand into one row

    # Player make a bet
    def bet(self):
        print(f'Your current deposit is: {self.deposit}$')
        print('Choose your bet')
        sleep(0.1)
        amount = input('$:')
        while True:
            if self.deposit == 0:  # going all in with additional bet
                print("You have no more money to make a bet. You are going all-in!")
                return 0
            if not amount.isdigit():  # invalid input
                print('Choose your bet')
                sleep(0.1)
                amount = input('$:')
            elif int(amount) > self.deposit:  # invalid input
                print(f"You don't have enough money. Your current deposit is: {self.deposit}\nTry smaller bet")
                print('Choose your bet')
                sleep(0.1)
                amount = input('$:')
            elif int(amount) <= 0:  # invalid input
                print('Choose your bet')
                sleep(0.1)
                amount = input('$:')
            else:  # valid input
                amount = int(amount)   # bet
                self.deposit -= amount
                sleep(0.1)
                print(f'Your bet is {amount}$. Your current deposit is: {self.deposit}$')
                sleep(0.1)
                return amount

    # Bet before taking additional cards
    def additional_bet(self):
        print(f'Your current deposit is: {self.deposit}$')
        print('Press B to make additional bet or press P for Pass')
        sleep(0.1)
        amount = 0  # Bet value
        while True:
            key = keyboard.read_key()
            if key == "p":  # skip bet
                sleep(0.3)
                print('Pass')
                sleep(0.3)
                break
            elif key == "b":  # make additional bet
                sleep(0.3)
                amount = self.bet()
                sleep(0.3)
                break
            else:  # invalid choice
                sleep(0.2)
                print('Press B to make additional bet or press P for Pass')
                sleep(0.2)
        return amount

    # Check if player has blackjack
    def bj_check(self):
        return self.hand_sum() == 21

    # Check if player has more than 21 points and loose
    def loose(self):
        return self.hand_sum() > 21

    # Check if player lost all deposit
    def no_money(self):
        return self.deposit == 0

    # Print player's name and points in hand, deposit
    def __str__(self):
        return f'{self.name} has {self.hand_sum()} points. Current deposit: {self.deposit}$'

