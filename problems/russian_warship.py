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

# done "Clear sea" initialisation function
# done Output function with 'clear screen' feature
# done intro
# done Random warships initialisation
# done Random shot
# done User shot
# inpr Primitive game

# - (request for the size of the field)
# - (request for the ship allocation mode (auto or manual))
# - (auto allocation function)
#   (- random allocation with the checks of allocation laws and crossections)
# - (manual allocation function)
#   (- manual allocation function with the checks of allocation laws and crossections)
# - (optional colour output)
# - game function
#   - game with computer (no strategy, only random shots with checks of previuos shot locations. Not shooting twice in one location)
#   - game with computer with a primitive strategy (trying to catch big ships shooting to the locations nearby to the successful hits)
#   - game with the friend on the other screen (saving game state into the json file and updating state after each shot)
#   - game with the friend using cloud files storage (e.g. dropbox of google drive, updating files after each save action)
#   - 


import os
import json
import random
from time import sleep



def clear_terminal():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def war_sea_initiate(longitude_size=10, latitude_size=13):
    war_sea = [['~' for i in range(longitude_size)] for j in range(latitude_size)]
    return war_sea


def random_ships_location(war_sea, size, quantity):
    
    for _ in range(quantity):

        built = False
        while not built:

            i = random.randint(0, 9)
            j = random.randint(0, 12)
            d = random.randint(0, 1)
            taken_place = False

            if d == 0:

                if i + size > len(war_sea[0]):
                    continue
                
                for step in range(size):
                    if not war_sea[j][i+step] == '~':
                        taken_place = True
                
                if taken_place == False:
                    for step in range(size):
                        war_sea[j][i+step] = 'S'
                        built = True
                else:
                    continue

            elif d == 1:
                
                if j + size > len(war_sea):
                    continue
                
                for step in range(size):
                    if not war_sea[j+step][i] == '~':
                        taken_place = True
                
                if taken_place == False:
                    for step in range(size):
                        war_sea[j+step][i] = 'S'
                        built = True
                else:
                    continue

    return war_sea


def make_sea_subframe(sea: list, header: str, start_indentation: str, middle_indentation: str):

    sea_subframe = []
    sea_subframe.append(header)
    for index, row in enumerate(sea):
        if index < 9:
            line_number = ' ' + str(index+1)
        else:
            line_number = str(index+1)
        line = line_number + '  '
        for element in row:
            line = line + element + '  '
        sea_subframe.append(line)
    return sea_subframe


def make_frame(my_war_sea: list, hostile_war_sea: list):
    
    total_frame = []
    my_sea_subframe = []
    hostile_sea_subframe = []
    header = '    A  B  C  D  E  F  G  H  I  J  '
    start_indentation = '   '
    middle_indentation = '     '

    my_sea_subframe = make_sea_subframe(my_war_sea, header, start_indentation, middle_indentation)
    hostile_sea_subframe = make_sea_subframe(hostile_war_sea, header, start_indentation, middle_indentation)
    
    # trying to make frame
    for index in range(len(my_sea_subframe)):
        line = start_indentation + my_sea_subframe[index] + middle_indentation + hostile_sea_subframe[index]
        total_frame.append(line)
    
    return total_frame


def print_frame(frame):

    clear_terminal()
    for line in frame:
        # sleep(0)
        print(line)


def random_shot(war_sea: list):
    
    shot = False
    hit = 0
    while not shot:
        i = random.randint(0,9)
        j = random.randint(0,12)

        if (war_sea[j][i]) == 'X' or (war_sea[j][i] == ' '):
            continue
        elif war_sea[j][i] == 'S':
            war_sea[j][i] = 'X'
            hit += 1
        elif war_sea[j][i] == '~':
            war_sea[j][i] = ' '
            shot = True
    return hit


def user_shot(war_sea: list):
    
    shot = False
    hit = 0
    while not shot:
        i = int(input('x coordinate: '))
        j = int(input('y coordinate: '))

        if (war_sea[j][i]) == 'X' or (war_sea[j][i] == 'o'):
            pass
        elif war_sea[j][i] == 'S':
            war_sea[j][i] = 'X'
            hit += 1
        elif war_sea[j][i] == '~':
            war_sea[j][i] = 'o'
            shot = True
    return hit



INTRO_MESSAGE = """
Близько 22:00, 24 лютого 2022 року, острів Зміїний, Україна.

- Остров Змєіний, я русскій воєнний корабль. Остров Змєіний, я русскій воєнний корабль.
  Прєдлагаю сложить оружиє і сдаться во ізбежаніе коровопролітія і неоправданних жертв. 
  В протівном случає по вам будєт нанєсьон бомбовий удар...

- Повторяю...
  Остров Змєіний, я русскій воєнний корабль. Остров Змєіний, я русскій воєнний корабль.
  Прєдлагаю сложить оружиє і сдаться во ізбежаніе коровопролітія і неоправданних жертв. 
  В протівном случає по вам будєт нанєсьон бомбовий удар...
"""

clear_terminal()

# for i in range(len(INTRO_MESSAGE)+1):
#     clear_terminal()
#     print(INTRO_MESSAGE[:i])
#     sleep(0.03)

sleep(0.5)
print('Дайте вашу відповідь окупантам, щоб почати гру:\n')
sleep(0.5)
answer = input('- рускій воєнний корабль, ')

if 'іді нахуй' in answer:
    sleep(0.5)
    print('\nВідповідь правильна, починаємо відлік до затоплення\n')
    sleep(0.5)

    my_war_sea = war_sea_initiate()
    hostile_war_sea = war_sea_initiate()

    random_ships_location(my_war_sea, 4, 1)
    random_ships_location(my_war_sea, 3, 2)
    random_ships_location(my_war_sea, 2, 3)
    random_ships_location(my_war_sea, 1, 4)

    frame = make_frame(my_war_sea, hostile_war_sea)

    print_frame(frame)

    random_ships_location(hostile_war_sea, size=4, quantity=1)
    random_ships_location(hostile_war_sea, size=3, quantity=2)
    random_ships_location(hostile_war_sea, size=2, quantity=3)
    random_ships_location(hostile_war_sea, size=1, quantity=4)

    frame = make_frame(my_war_sea, hostile_war_sea)

    print_frame(frame)


    # while True:
    #     user_hits = 0
    #     machine_hits = 0

    #     user_hits += random_shot(hostile_war_sea)
    #     frame = make_frame(my_war_sea, hostile_war_sea)
    #     print_frame(frame)
    #     sleep(0.1)
    #     machine_hits += random_shot(my_war_sea)
    #     frame = make_frame(my_war_sea, hostile_war_sea)
    #     print_frame(frame)
    #     sleep(0.1)


# hits = random_shot(my_war_sea)

# frame = make_frame(my_war_sea, hostile_war_sea)
# print_frame(frame)
# print(hits)

# hits = user_shot(hostile_war_sea)

# frame = make_frame(my_war_sea, hostile_war_sea)
# print_frame(frame)
# print(hits)