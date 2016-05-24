# Aaren
from constant import *
from ClueGame import *

def print_welcome_text():
    print("Welcome to the clue solver\n")

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
            player_i_cards = get_int_stdin("How many cards does " + player_i_name + " have? ")
            print("\n")
            player_dictionary[player_i_name] = player_i_cards
            i += 1
    debug(player_dictionary)
    return player_dictionary

def get_game_option():
    print("For Right Now We're assuming you want to use the default board")
    return DEFAULT_GAME


if __name__=="__main__":
    print_welcome_text()
    players = get_game_players()
    game_option = get_game_option()
    a = ClueGame( players , game_option )
    a.enter_game_loop()
