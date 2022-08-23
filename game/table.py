from time import sleep
import keyboard
from game.cards import Deck
from game.player import Player
from game.dealer import Dealer


# Create playing table class
class Table:

    # Creating a new playing table with a player, dealer as a casino, and new shuffled deck
    def __init__(self, name_player):
        self.game_on = True
        self.bank = 0
        self.new_deck = Deck()
        self.casino = Dealer()
        self.amount = 0
        self.second_bet_amount = 0
        self.gamer = Player(name_player)

    # Print actual bank on the table
    def __str__(self):
        return f'Bank is {self.bank}'

    # Reset hands
    def reset(self):
        # Empty players hand
        self.gamer.hand = []
        self.casino.hand = []
        self.new_deck.deck_shuffle()

    # Deal 2 cards to dealer and player
    def first_deal(self):
        self.reset()  # reset table
        print(self.casino.depos())  # casino deposit
        self.amount = self.gamer.bet()  # player bet
        self.casino.deposit -= self.amount  # dealer bet
        self.bank += self.amount * 2  # bank
        print('Player got 2 cards from Dealer')
        sleep(0.3)
        # Deal two cards to player
        self.gamer.add_two(self.new_deck.all_cards.pop(0), self.new_deck.all_cards.pop(1))
        self.gamer.show_hand()  # print player hand
        print(self.gamer)
        sleep(0.3)
        print('Dealer got two cards')
        # Deal two card to dealer
        sleep(0.3)
        self.casino.add_two(self.new_deck.all_cards.pop(0), self.new_deck.all_cards.pop(1))
        self.casino.show_first_hand()  # print first dealer hand
        sleep(0.3)

    # Check if someone has blackjack
    def blackjack_check(self):
        # Player and dealer both have BJ. No one wins
        if self.gamer.bj_check() and self.casino.bj_check():
            sleep(0.3)
            self.casino.show_hand()
            sleep(0.3)
            print("It's a push! Bets were returned.")
            # returning bets
            self.gamer.deposit += self.amount
            self.casino.deposit += self.amount
            self.bank = 0
            return True
        # Player has BJ and win
        elif self.gamer.bj_check():
            sleep(0.3)
            self.casino.show_hand()
            sleep(0.3)
            print(f'{self.gamer.name} has a BlackJack! He wins {self.bank}$')
            self.gamer.deposit += self.bank
            self.bank = 0
            # Check if someone has no money to continue
            if self.no_more_money():
                self.game_on = False
            return True
        # Dealer has BJ and win
        elif self.casino.bj_check():
            sleep(0.3)
            print('Dealer cards:')
            self.casino.show_hand()
            print(f'Casino has a BlackJack! It wins {self.bank}$')
            self.casino.deposit += self.bank
            self.bank = 0
            sleep(0.3)
            # Check if someone has no money to continue
            if self.no_more_money():
                self.game_on = False
            return True
        else:
            return False

    # player make a second bet after getting 2 first cards
    def second_bet(self):
        self.second_bet_amount = self.gamer.additional_bet()  # second bet amount
        self.casino.deposit -= self.second_bet_amount  # dealer bet
        self.bank += self.second_bet_amount * 2  # bank
        self.deal_additional_card()  # deal cards

    # Check if players have enough money to continue
    def no_more_money(self):
        # Check player deposit
        if self.gamer.no_money():
            sleep(0.3)
            print('Player has no more money to play. You loose! Exit to menu')
            sleep(0.3)
            self.game_on = False
            return True
        # Check casino deposit
        if self.casino.no_money():
            sleep(0.3)
            print('Casino has no more money to play. Casino closed. Exit to menu')
            sleep(0.3)
            self.game_on = False
            return True
        return False

    # Deal cards to player if he wants
    def deal_additional_card(self):
        print('Press C to get another card. Press P to pass.')
        while True:
            # Ask player if he wants to pass or take a card
            key = keyboard.read_key()
            if key == "c":
                # take another card
                sleep(0.2)
                print()
                self.gamer.add_card(self.new_deck.all_cards.pop(0))
                self.gamer.show_hand()
                print(self.gamer)
                sleep(0.2)
                # check for overdraft
                if self.gamer.loose():
                    print(f'You loose! Your points is {self.gamer.hand_sum()}')
                    break
                print('Press C to get another card. Press P to pass')
                sleep(0.3)
            # check for pass
            elif key == "p":
                sleep(0.3)
                print('Pass')
                sleep(0.3)
                break
            # something else pressed
            else:
                sleep(0.3)
                print('Press C to get another card. Press P to pass')
                sleep(0.3)

    # Check if player want to continue playing or not
    def continue_playing(self):
        print('Do you want to continue playing or exit to menu? Press C to continue or E to exit')
        # ask for continue or exit to menu
        while True:
            key = keyboard.read_key()
            if key == "c":  # continue playing
                sleep(0.3)
                return True
            elif key == "e":  # exit to menu
                sleep(0.3)
                self.game_on = False
                return False
            else:  # wrong input
                sleep(0.3)
                print('Do you want to continue playing or exit to menu? Press C to continue or E to exit')
                sleep(0.3)

    # Flag to check if player have money to play
    def check_if_can_continue(self):
        return self.gamer.deposit > 0 and self.casino.deposit > 0

    # Check if player loosed
    def gamer_loose(self):
        print('Dealer cards:')
        sleep(0.3)
        self.casino.show_hand()
        sleep(0.3)
        print(f'{self.gamer.name} has {self.gamer.hand_sum()}! Overdraft! Casino '
              f'wins! {self.bank}$')
        sleep(0.3)
        self.casino.deposit += self.bank
        self.bank = 0

    # Check if casino loosed
    def casino_loose(self):
        print('Dealer cards:')
        sleep(0.3)
        self.casino.show_hand()
        print(f'Casino has {self.casino.hand_sum()}! Overdraft! Player '
              f'wins! {self.bank}$')
        sleep(0.3)
        self.gamer.deposit += self.bank
        self.bank = 0

    # Check if push
    def push(self):
        sleep(0.3)
        print('Dealer cards:')
        self.casino.show_hand()
        sleep(0.3)
        print("It's a push! Bets were returned.")
        sleep(0.3)
        self.gamer.deposit += self.amount + self.second_bet_amount  # return bet
        self.casino.deposit += self.amount + self.second_bet_amount  # return bet
        self.bank = 0

    # If player wins
    def gamer_win(self):
        sleep(0.3)
        print('Dealer cards:')
        sleep(0.3)
        self.casino.show_hand()
        sleep(0.3)
        print(
            f'{self.gamer.name} has {self.gamer.hand_sum()}! Dealer has {self.casino.hand_sum()}. Player '
            f'wins! {self.bank}$')
        sleep(0.3)
        self.gamer.deposit += self.bank  # bank goes to player
        self.bank = 0

    # If casino wins
    def casino_win(self):
        sleep(0.3)
        print('Dealer cards:')
        self.casino.show_hand()
        sleep(0.3)
        print(
            f'{self.gamer.name} has {self.gamer.hand_sum()}! Dealer has {self.casino.hand_sum()}. Casino '
            f'wins! {self.bank}$')
        sleep(0.3)
        self.casino.deposit += self.bank  # bank goes to casino
        self.bank = 0

