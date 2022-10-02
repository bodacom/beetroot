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
    sea_subframe.append(' ')
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
    frame_header = ' '
    header = '    A  B  C  D  E  F  G  H  I  J  '
    start_indentation = '   '
    middle_indentation = '     '

    my_sea_subframe = make_sea_subframe(my_war_sea, header, start_indentation, middle_indentation)
    hostile_sea_subframe = make_sea_subframe(hostile_war_sea, header, start_indentation, middle_indentation)
    total_frame.append(frame_header)
    for index in range(len(my_sea_subframe)):
        line = start_indentation + my_sea_subframe[index] + middle_indentation + hostile_sea_subframe[index]
        total_frame.append(line)
    
    return total_frame


def print_frame(frame):

    clear_terminal()
    print('\n       russian warship\n')
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
            shot = True
        elif war_sea[j][i] == '~':
            war_sea[j][i] = ' '
            shot = True
    return hit


def user_shot(war_sea: list, war_sea_hiden: list):
    
    shot = False
    hit = 0
    while not shot:
        coordinate = input('\n\n    Input XY coordinate to make a shot: ')
        coordinate = coordinate.upper()
        letters = 'ABCDEFGHIJ'
        if 2 <= len(coordinate) <= 3 and coordinate[0] in letters and coordinate[1:].isdigit() and 1 <= int(coordinate[1:]) <= 13:
            i = letters.find(coordinate[0])
            j = int(coordinate[1:])-1
        else:
            print('Невірний формат координат. Повторіть введення.')
            continue
         
        if (war_sea[j][i]) == 'X' or (war_sea[j][i] == 'o'):
            print('\n    Ups, you have already shoot the location.')
            sleep(2)
            break
        elif war_sea[j][i] == 'S':
            war_sea[j][i] = 'X'
            war_sea_hiden[j][i] = 'X'
            hit += 1
            shot = True
        elif war_sea[j][i] == '~':
            war_sea[j][i] = 'o'
            war_sea_hiden[j][i] = 'o'
            shot = True
    return hit


def play_intro(INTRO_MESSAGE):
    
    clear_terminal()

    for i in range(len(INTRO_MESSAGE)+1):
        clear_terminal()
        print(INTRO_MESSAGE[:i])
        sleep(0.03)

    sleep(0.5)
    print('Дайте вашу відповідь окупантам, щоб почати гру:\n')
    sleep(0.5)


def request_for_password():
    
    status = False
    while not status:
        answer = input('- рускій воєнний корабль, ')
        if 'іді нахуй' or 'иди нахуй' in answer:
            status = True
            if status:
                continue
            print('Відповідь неправильна, спробуйте ще раз.')

    sleep(1.5)
    print('\nВідповідь правильна, починаємо відлік до затоплення\n')
    sleep(1.5)




# Main cycle

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


# initiating the war seas

my_war_sea = war_sea_initiate()
hostile_war_sea = war_sea_initiate()
hostile_war_sea_hiden = war_sea_initiate()



# initiating the war ships

for i in range(1, 5):
    random_ships_location(my_war_sea, i, 5-i)
    random_ships_location(hostile_war_sea, i, 5-i)

user_ships = 20
machine_ships = 20


#random choice of the first shooter
who_shoots = random.randint(0, 1)
user_hits = 0
machine_hits = 0

sleep_time = 1.2

play_intro(INTRO_MESSAGE)

request_for_password()

# main game cycle

while True:

  # Refresh game screen print
    
    frame = make_frame(my_war_sea, hostile_war_sea_hiden)
    print_frame(frame)
    
    print(f'\n    Your ships left: {user_ships}            russian ships left: {machine_ships}')
    
    if who_shoots == 0:
        print('\n    Your shot', end='')
    else:
        print('\n    Enemy shot', end='')

    sleep(sleep_time)
  # Shooting

    if who_shoots == 0:
        hit_result = user_shot(hostile_war_sea, hostile_war_sea_hiden)
        user_hits += hit_result
        machine_ships -= hit_result
    else:
        hit_result = random_shot(my_war_sea)
        machine_hits += hit_result
        user_ships -= hit_result


  # Refreshing screen

    frame = make_frame(my_war_sea, hostile_war_sea_hiden)
    print_frame(frame)

    if machine_ships == 0:
        #clear_terminal()
        print(f'\n    Game Over\n     You win\n   Your ships left: {user_ships}            russian ships left: {machine_ships}')
        break
    elif user_ships == 0:
        #clear_terminal()
        print(
            f'\n    Game Over\n     You loose\n   Your ships left: {user_ships}            russian ships left: {machine_ships}')
        break

    else:
        print(f'\n    Your ships left: {user_ships}            russian ships left: {machine_ships}')
    
    if hit_result > 0 and who_shoots == 0:
        print('\n    Nice shot! You hit the ship! One more shot for you.', end='')
        sleep(sleep_time)
        continue
    elif who_shoots == 0 and hit_result == 0:
        print('\n    You missed, sorry.', end='')

    if who_shoots == 1 and hit_result > 0:
        print('\n    Yay! You lost the ship! One more shot for the enemy', end='')
        sleep(sleep_time)
        continue
    elif who_shoots == 1 and hit_result == 0:
        print('\n    Enemy missed, you are lucky.', end='')

  # Changing the shooter

    if who_shoots == 0:
        who_shoots = 1
    else:
        who_shoots = 0

    sleep(sleep_time)
