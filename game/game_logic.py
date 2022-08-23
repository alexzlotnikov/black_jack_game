from time import sleep
import keyboard
from game.table import Table

# default name
name_player = "Player"


# get player name
def get_name():
    global name_player
    print('Welcome to our Casino!')
    name_player = input('Please, enter you name:\n')
    menu()  # go to menu


# Enter the menu
def menu():
    sleep(0.2)
    print('\nDo you want to play BlackJack?\nPress Y to play, N for exit')
    while True:
        key = keyboard.read_key()
        if key == "y":  # Y to play
            sleep(0.2)
            print()
            game()
            break
        elif key == "n":  # N to exit
            sleep(0.2)
            print()
            print('Goodbye!')
            break
        else:  # Something else pressed
            sleep(0.2)
            print('Press Y to play, N for exit')
            sleep(0.2)


# Game flow
def game():
    table = Table(name_player)  # Creating new table
    while table.game_on:  # check if game active
        while table.check_if_can_continue():  # check if players have enough money
            # Empty players hand and shuffle deck
            table.reset()
            # Deal first cards
            table.first_deal()
            # Check for blackjacks
            if not table.blackjack_check():
                # no BJ
                table.second_bet()
                # Check if player lost
                if table.gamer.loose():
                    # Player has overdraft and loose
                    table.gamer_loose()
                    break
                # check if enough money to continue
                if table.no_more_money():
                    break
                # Dealer take cards
                while table.casino.hand_sum() < table.casino.max_point:
                    table.casino.add_card(table.new_deck.all_cards.pop(0))
                # check if dealer lost
                if table.casino.loose():
                    # Casino has overdraft and loose
                    table.casino_loose()
                    break
                # check if enough money to continue
                if table.no_more_money():
                    break
                # Check who won
                if table.gamer.hand_sum() == table.casino.hand_sum():
                    # Player and dealer both have same points. No one wins
                    table.push()
                elif table.gamer.hand_sum() > table.casino.hand_sum():
                    # Player has more points and win
                    table.gamer_win()
                elif table.gamer.hand_sum() < table.casino.hand_sum():
                    # Dealer has more points and win
                    table.casino_win()
                # Check if someone has no money to continue
                if table.no_more_money():
                    break
            # Ask player to continue or not
            if table.continue_playing():
                # Clear hands and shuffle new deck
                table.reset()
            else:
                sleep(0.3)
                # exit to menu
                menu()




