# Aaren Barge

DEFAULT_GAME = {1 : "Colnel Mustard" ,
                2 : "Professor Plum" ,
                3 : "Mr. Green" ,
                4 : "Mrs. Peacock" ,
                5 : "Miss Scarlet" ,
                6 : "Mrs. White" ,
                7 : "Knife" ,
                8 : "Candlestick" ,
                9 : "Revolver" ,
                10 : "Rope" ,
                11 : "Lead Pipe" ,
                12 : "Wrench" ,
                13 : "Hall" ,
                14 : "Lounge" ,
                15 : "Dining Room" ,
                16 : "Kitchen" ,
                17 : "Ballroom" ,
                18 : "Conservatory" ,
                19 : "Billiard Room" ,
                20 : "Library" ,
                21 : "Study"
                                        }

# Function used to debug output easily
DEBUG_MODE = True
DEBUG_LEVEL = 0
def debug(str_to_print, level):
    if DEBUG_MODE and level > DEBUG_LEVEL:
        print str_to_print
