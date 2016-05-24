# Aaren Barge

class Player:

    def __init__(self, playername, cardnum):
        self.player_name = playername
        self.num_cards = cardnum

    def get_player_name(self):
        return self.player_name

    def get_player_cardnum(self):
        return self.cardnum
