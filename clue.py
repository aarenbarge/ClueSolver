# Aaren
from constant import *
from ClueGame import *

def print_welcome_text():
    print("Welcome to the clue solver")
    print("Press control-c to stop at any time\n")

def get_int_stdin(message):
    found = False
    to_return = ""
    while not found:
        try:
            to_return = int(raw_input(message))
            found = True
        except ValueError:
            print "Not a Valid Number, try again:"
    return to_return

###########################################################
# SUMMARY - get_game_players
###########################################################
# DEBUG LEVEL 1
# Returns a dictionary of {"Player Name" : Number of Cards}
# Enforces the conditions:
#   Names must be unique, this is not case sensitive
#   Name must not be "You", this is not case sensitive
#   Number of cards must be a positive integer
# Loops until all of these conditions are met, asking to "try again" if
# An entry is incorrect
###########################################################

###########################################################
# DEPENDENCIES
###########################################################
# get_int_stdin()   | clue.py
###########################################################

###########################################################
# Testing
###########################################################
# - File Name : Test for what condition
###########################################################

def get_game_players():
    player_dictionary = {}
    print("How many players (including yourself) are playing this game?")
    num_players = get_int_stdin("")
    your_cards = get_int_stdin("How many cards do YOU have? ")
    player_dictionary["You"] = your_cards
    i = 1
    while i < num_players:
        player_i_name = raw_input("Name of Player " + str(i) + ": ")
        if (player_i_name.upper() in [x.upper() for x in player_dictionary.keys() + ["You"]] ):
            print("Invalid Player Name, try again")
        else:
            found = False
            while not found:
                player_i_cards = get_int_stdin("How many cards does " + player_i_name + " have? ")
                if player_i_name <= 0:
                    print("Number of cards for a player must be positive, try again")
                else:
                    found = True
            print("\n")
            player_dictionary[player_i_name] = player_i_cards
            i += 1
    debug(player_dictionary,1)
    return player_dictionary

def get_game_option():
    print("For Right Now We're assuming you want to use the default board")
    return DEFAULT_GAME

def print_game_option(game_option):
    number_header = "Number"
    item_header = "Item"
    print("\n\nThe following shows the game options. These can be reprinted any time by using the command \":p\"")
    largest_num = len(str(max(game_option.keys())))
    if largest_num < len(number_header):
        largest_num = len(number_header)
    largest_len = max([len(x) for x in game_option.values()])
    if largest_len < len(item_header):
        largest_len = len(item_header)
    print(("{:<" + str(largest_num) + "} {:<" + str(largest_len) + "}").format(number_header,item_header))
    for v in sorted(game_option.keys()):
        label = game_option[v]
        print(("{:<" + str(largest_num) + "} {:<" + str(largest_len) + "}").format(v, label))
    print("\n\n")

def get_your_cards(num_cards, max_num):
    cards = []
    print("Enter the number of each card you have in your hand:\n")
    i = 1
    while i <= num_cards:
        card_i = get_int_stdin("Card " + str(i) + ": ")
        if card_i <= 0 or card_i > max_num or card_i in cards:
            print("Invalid, try again")
        else:
            cards.append(card_i)
            i += 1
    debug(cards, 1)
    return cards


if __name__=="__main__":
    print_welcome_text()
    players = get_game_players()
    game_option = get_game_option()
    print_game_option(game_option)
    your_cards = get_your_cards(players["You"],max(game_option.keys()))
    a = ClueGame( players , game_option , your_cards)
    a.enter_game_loop()
