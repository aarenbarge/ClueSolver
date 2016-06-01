# Aaren Barge
SUSPECT = 1
WEAPON = 2
ROOM = 3
DEFAULT_GAME = {1 : ("Colnel Mustard",SUSPECT) ,
                2 : ("Professor Plum",SUSPECT) ,
                3 : ("Mr. Green",SUSPECT) ,
                4 : ("Mrs. Peacock",SUSPECT) ,
                5 : ("Miss Scarlet",SUSPECT) ,
                6 : ("Mrs. White",SUSPECT) ,
                7 : ("Knife",WEAPON) ,
                8 : ("Candlestick",WEAPON) ,
                9 : ("Revolver",WEAPON) ,
                10 : ("Rope",WEAPON) ,
                11 : ("Lead Pipe",WEAPON) ,
                12 : ("Wrench",WEAPON) ,
                13 : ("Hall",ROOM) ,
                14 : ("Lounge",ROOM) ,
                15 : ("Dining Room",ROOM) ,
                16 : ("Kitchen",ROOM) ,
                17 : ("Ballroom",ROOM) ,
                18 : ("Conservatory",ROOM) ,
                19 : ("Billiard Room",ROOM) ,
                20 : ("Library",ROOM) ,
                21 : ("Study",ROOM)
                                        }

# Function used to debug output easily
DEBUG_MODE = True
DEBUG_LEVEL = 0
def debug(str_to_print, level):
    if DEBUG_MODE and level > DEBUG_LEVEL:
        print str_to_print

import time
DEBUG_START_TIME = 0
DEBUG_END_TIME = 0
def start_debug_time():
    global DEBUG_START_TIME
    DEBUG_START_TIME = time.time()
def end_debug_time(message):
    global DEBUG_END_TIME
    DEBUG_END_TIME = time.time()
    debug("DEBUG: timing:\"" + message + "\" time: " + str(DEBUG_END_TIME - DEBUG_START_TIME),1)
