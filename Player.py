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
        self.one_of = []
        for i in range(1,max_cards+1):
            self.could_have.append(i)
            self.could_have = sorted(self.could_have)
        self.possibilities = self.generate_possibilities(self.num_cards, self.could_have)
        debug(len(self.possibilities),2)

    def get_possibilities(self):
        return self.possibilities

    def get_definitely_has(self):
        return self.definitely_has

    def get_doesnt_have(self):
        return self.doesnt_have

    def get_could_have(self):
        return self.could_have

    def get_one_of(self):
        return self.one_of

    def is_solved(self):
        return self.solved

    def print_summary(self):
        print "Name: " + str(self.player_name)
        print "is_solved: " + str(self.solved)
        print "definitely_has: " + str(self.definitely_has)
        print "doesnt_have: " + str(self.doesnt_have)
        print "might have: " + str(self.could_have)
        print "one_ofs: " + str(self.one_of)

    def doesnt_have_card(self,num):
        start_debug_time()
        if num not in self.doesnt_have and self.solved == False:
            self.doesnt_have.append(num)
            self.doesnt_have = sorted(self.doesnt_have)
            self.could_have.remove(num)
            dels = []
            for pos in self.possibilities:
                if num in pos:
                    dels.append(pos)
            for d in dels:
                self.possibilities.remove(d)
            self.update_deck()
            end_debug_time("doesnt_have_card")
            return 1
        else:
            end_debug_time("doesnt_have_card unsuccesful")
            return 0

    def has_card(self,num):
        start_debug_time()
        if num not in self.definitely_has and self.solved == False:
            self.definitely_has.append(num)
            self.definitely_has = sorted(self.definitely_has)
            self.could_have.remove(num)
            dels = []
            for pos in self.possibilities:
                if num not in pos:
                    dels.append(pos)
            for d in dels:
                self.possibilities.remove(d)
            for pos in self.possibilities:
                pos.remove(num)
            self.update_deck()
            end_debug_time("has_card")
            return 1
        else:
            end_debug_time("has_card unsuccesful")
            return 0

    def has_one_of(self,nums):
        start_debug_time()
        if len(nums) == 3 and len( [ x for x in nums if x in self.definitely_has ] ) == 0:
            if sorted(nums) not in self.one_of:
                self.one_of.append((sorted(nums),False))
                dels = []
                for pos in self.possibilities:
                    if nums[0] not in pos and nums[1] not in pos and nums[2] not in pos:
                        dels.append(pos)
                for d in dels:
                    self.possibilities.remove(d)
                self.update_deck()
                end_debug_time("has_one_of")
                return 1
        end_debug_time("has_one_of unsuccesful")
        return 0

    def update_deck(self):
        if len(self.definitely_has) == self.num_cards:
            self.solved = True
            self.possibilities = []
        else:
            updated = True
            while updated == True:
                print "inside while updated"
                updated = False
                temp_not_found_list = self.could_have
                in_none = []
                in_some = []
                in_all = []
                first = True
                for pos in self.possibilities:
                    if first == True:
                        for num in temp_not_found_list:
                            if num in pos:
                                in_all.append(num)
                            else:
                                in_none.append(num)
                        first = False
                    else:
                        for num in (in_none + in_all):
                            if num in in_none and num in pos:
                                in_none.remove(num)
                                in_some.append(num)
                            if num in in_all and num not in pos:
                                in_all.remove(num)
                                in_some.append(num)
                for num in in_none:
                    if num not in self.doesnt_have:
                        self.doesnt_have_card(num)
                        updated = True
                for num in in_all:
                    if num not in self.definitely_has:
                        self.has_card(num)
                        updated = True
        if len(self.definitely_has) == self.num_cards:
            self.solved = True
            self.possibilities = []


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
