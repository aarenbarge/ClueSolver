from constant import *
from Player import *

class ClueGame:

    # players_map {"players name" : num_cards}
    # game_type {card_id : "Card Name"}
    def __init__( self, players_map , game_type , your_cards):
        # Enforce Pre-conditions
        num_game_cards = len(game_type.keys())
        num_player_cards = sum( [players_map[x] for x in players_map.keys()] )
        if (num_game_cards) != (num_player_cards + 3): # 3 Cards are in the envelope
            print("error: wrong number of cards given")
            quit() # TODO : Find a better way of throwing these errors

        # Setup the game
        self.players_map = {player_name : Player(playername=player_name, cardnum=players_map[player_name], game_type=game_type ) for player_name in players_map.keys()}
        for card in your_cards:
            self.players_map["You"].has_card(card)
        
        print "okay"

    def enter_game_loop(self):
        print("playing Clue!")
