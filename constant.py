# Aaren Barge

DEFAULT_GAME = {1 : ("Colnel Mustard",1) ,
                2 : ("Professor Plum",1) ,
                3 : ("Mr. Green",1) ,
                4 : ("Mrs. Peacock",1) ,
                5 : ("Miss Scarlet",1) ,
                6 : ("Mrs. White",1) ,
                7 : ("Knife",2) ,
                8 : ("Candlestick",2) ,
                9 : ("Revolver",2) ,
                10 : ("Rope",2) ,
                11 : ("Lead Pipe",2) ,
                12 : ("Wrench",2) ,
                13 : ("Hall",3) ,
                14 : ("Lounge",3) ,
                15 : ("Dining Room",3) ,
                16 : ("Kitchen",3) ,
                17 : ("Ballroom",3) ,
                18 : ("Conservatory",3) ,
                19 : ("Billiard Room",3) ,
                20 : ("Library",3) ,
                21 : ("Study",3)
                                        }

# Function used to debug output easily
DEBUG_MODE = True
DEBUG_LEVEL = 0
def debug(str_to_print, level):
    if DEBUG_MODE and level > DEBUG_LEVEL:
        print str_to_print
