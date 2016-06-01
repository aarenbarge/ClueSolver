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
        self.other_players = [x for x in players_map.keys() if x != "You"]
        for card in your_cards:
            self.players_map["You"].has_card(card)
            for PLAYER in self.other_players:
                self.players_map[PLAYER].doesnt_have_card(card)
        print "okay"

    def update_records(self):


    def record_information(self, player_name, cards, result):
        playername = [x for x in self.players_map if x.upper() == player_name.upper()]
        if len(playername) == 0:
            print "have a problem finding him"
        if len(playername) > 1:
            print "too many wut?"
        player = playername[0]
        if result == 1:
            # player has the card
            self.players_map[player].has_one_of(cards)
        else:
            self.players_map[player].doesnt_have_card(cards[0])
            self.players_map[player].doesnt_have_card(cards[1])
            self.players_map[player].doesnt_have_card(cards[2])
        self.update_records()

    def enter_game_loop(self):
        print("playing Clue!")
        self.record_information("Mom",[1,2,9],1)
        self.record_information("Mom",[2,7,10],1)
        self.record_information("Mom",[7,11,12],0)
        self.players_map["Mom"].print_summary()
