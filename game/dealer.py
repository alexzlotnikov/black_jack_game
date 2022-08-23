# Creating a Dealer class
class Dealer:

    # Create a Dealer with empty hand and basic deposit
    def __init__(self):
        self.name = 'Dealer'
        self.hand = []
        self.deposit = 1000
        self.max_point = 17

    # Deal first 2 cards to dealer
    def add_two(self, new_card1, new_card2):
        self.hand.append(new_card1)
        self.hand.append(new_card2)

    # Deal one card to dealer
    def add_card(self, new_card):
        if self.hand_sum() < self.max_point:
            self.hand.append(new_card)

    # Printing first dealer hand with first card opened and second closed
    def show_first_hand(self):
        print('\n'.join(map('  '.join, zip(*(self.hand[0].show_face(), self.hand[0].show_back())))))

    # Print all cards in dealer hand
    def show_hand(self):
        print('\n'.join(map('  '.join, zip(*(c.show_face() for c in self.hand)))))

    # Count how many point dealer has
    def hand_sum(self):
        hand_values = [card.value for card in self.hand]
        if 1 in hand_values and sum(hand_values) <= 11:
            return sum(hand_values) + 10
        else:
            return sum(hand_values)

    # Check if dealer has blackjack
    def bj_check(self):
        return self.hand_sum() == 21

    # Check if Dealer loose
    def loose(self):
        return self.hand_sum() > 21

    # Check if dealer has enough money
    def no_money(self):
        return self.deposit == 0

    # Print points in dealer hand and his deposit
    def __str__(self):
        return f'Dealer has {self.hand_sum()} points. Casino deposit: {self.deposit}$'

    # Show current casino deposit
    def depos(self):
        return f'Casino deposit: {self.deposit}$'
