# Sea Battle game named after famous story about russian warship 'moscow'

# To make a console Sea Battle game 
# (Start window)

#    A  B  C  D  E  F  G  H  I  J       A  B  C  D  E  F  G  H  I  J
#  1 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~     1 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
#  2 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~     2 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
#  3 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~     3 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
#  4 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~     4 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
#  5 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~     5 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
#  6 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~     6 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
#  7 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~     7 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
#  8 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~     8 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
#  9 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~     9 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
# 10 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~    10 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
# 11 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~    11 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
# 12 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~    12 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~
# 13 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~    13 ~  ~  ~  ~  ~  ~  ~  ~  ~  ~

#   ABCDEFGHIJ
#  1~~~~~~~~~~
#  2~~~~x~X~~~
# - request for the size of the field
# - request for the ship allocation mode (auto or manual)
# - auto allocation function
#   - random allocation with the checks of allocation laws and crossections
# - manual allocation function
#   - manual allocation function with the checks of allocation laws and crossections
# - output function with clear screen feature
# - optional colour output
# - game function
#   - game with computer (no strategy, only random shots with checks of previuos shot locations. Not shooting twice in one location)
#   - game with computer with a primitive strategy (trying to catch big ships shooting to the locations nearby to the successful hits)
#   - game with the friend on the other screen (saving game state into the json file and updating state after each shot)
#   - game with the friend using cloud files storage (e.g. dropbox of google drive, updating files after each save action)
#   - 


import os
import json
from time import sleep


def clear_terminal():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def war_sea_initiate(longitude_size = 10, latitude_size = 13):
    war_sea = [['~' for i in range(longitude_size)] for j in range(latitude_size)]
    return war_sea


def print_war_sea(war_sea):
    
    clear_terminal()
    print('    A  B  C  D  E  F  G  H  I  J        A  B  C  D  E  F  G  H  I  J')
    print()

    for index, row in enumerate(war_sea):
        for i in range(2):
            if index < 9:
                print(' ' + str(index+1) + ' ', end=' ')
            else:
                print(str(index+1) + ' ', end=' ')
            for element in row:
                print(element, end='  ')
        # print(sep_sea, end='')
        print()

    print()



war_sea = war_sea_initiate()

print_war_sea(war_sea)