# Aaren Barge

from constant import *

class Player:

    def __init__(self, playername, cardnum, game_type):
        max_cards = max(game_type.keys())
        self.solved = False
        self.player_name = playername
        self.num_cards = cardnum
        self.doesnt_have = []
        self.definitely_has = []
        self.could_have = [] # Could have needs to be sorted to work
        for i in range(1,max_cards+1):
            self.could_have.append(i)
            self.could_have = sorted(self.could_have)
        self.possibilities = self.generate_possibilities(self.num_cards, self.could_have)
        debug(len(self.possibilities),2)

    def is_solved(self):
        return self.solved

    def has_card(self,num):
        if num not in self.definitely_has and self.solved == False:
            self.definitely_has.append(num)
            self.definitely_has = sorted(self.definitely_has)
            dels = []
            for pos in self.possibilities:
                if num not in pos:
                    dels.append(pos)
            for d in dels:
                self.possibilities.remove(d)
            self.update_deck()
            return 1
        else:
            return 0

    def update_deck(self):
        if len(self.definitely_has) == self.num_cards:
            self.solved = True
            self.possibilities = [self.definitely_has]

    def generate_possibilities(self, depth, lis):
        if depth == 0 or lis == []:
            return []
        if depth == 1:
            return [ [x] for x in lis ]
        to_return = []
        for elem in lis:
            pos = self.generate_possibilities(depth-1, [x for x in lis if x > elem])
            for e in pos:
                if len([elem] + e) == depth:
                    to_return.append([elem] + e)
        return to_return

    def get_player_name(self):
        return self.player_name

    def get_player_cardnum(self):
        return self.cardnum
