from random import randint
import os


size_x = 9
size_y = 13
ship = "S"
water = "~"
hit = "X"
miss = "O"
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
ship_collection = {
    4: 1,
    1: 4,
    2: 3,
    3: 2,
    }


def generate_array():
    return [[water]*size_x for i in range(size_y)]


def print_fields(player_field: list, enemy_field: list):
    os.system('cls')
    
    text = "\t"
    
    for i in range(size_x):
        text += letters[i] + " "
    
    text += "\t|\t\t"
    
    for i in range(size_x):
        text += letters[i] + " "    
    
    text += "\n\n"
    hidden_field = []
    
    for i in range(len(enemy_field)):
        hidden_field.append(enemy_field[i].copy())
    
    for list in hidden_field:
        for i in range(len(list)):
            list[i] = list[i].replace(water, "?").replace(ship, "?")
            
    for list in range(size_y):
        text += f"{list + 1}\t{' '.join(player_field[list])}\t|\t{list + 1}\t{' '.join(hidden_field[list])}\n"
    
    print(text)
    print(f"Your score is: {get_score(enemy_field)}\t\t|\tEnemy score is: {get_score(player_field)}\n")


def place_ship(field: list, x: int, y: int, ship_size_x: int, ship_size_y: int):
    for i in range(x, x + ship_size_x):
        for j in range(y, y + ship_size_y):
            field[j][i] = ship


def try_place_ship_horizontal(field: list, x: int, y: int, ship_size: int):
    
    if ship_size > size_x or ship_size < 1:
        print("Ship size is incorrect")
        return False
    for i in range(ship_size):
        if check_cell(field, x + i, y) == False:
            return False
    for i in range(ship_size):
        field[y][x + i] = ship


def try_place_ship_vertical(field: list, x: int, y: int, ship_size: int):
    
    if ship_size > size_y or ship_size < 1:
        print("Ship size is incorrect")
        return False
    for i in range(ship_size):
        if check_cell(field, x, y + i) == False:
            return False
    for i in range(ship_size):
        field[y + i][x] = ship


def check_cell(field: list, x: int, y: int):
    if x < 0 or x >= size_x:
        return False
    if y < 0 or y >= size_y:
        return False

    x_max = x + 2
    x_min = x - 1
    y_max = y + 2
    y_min = y - 1
    
    if x_max > size_x:
        x_max = size_x
    if x_min < 0:
        x_min = 0
    if y_max > size_y:
        y_max = size_y
    if y_min < 0:
        y_min = 0

    for i in range(x_min, x_max):
        for j in range(y_min, y_max):
            if field[j][i] != water:
                return False
    
    return True


def get_valid_cells(field: list, ship_size_x: int, ship_size_y: int):
    valid_cells = []
    
    for i in range(size_x):
        for j in range(size_y):
            if does_ship_fit(field, i, j, ship_size_x, ship_size_y):
                valid_cells.append((i, j))
    
    return valid_cells


def does_ship_fit(field: list, x: int, y: int, ship_size_x: int, ship_size_y: int):
    for i in range(x, x + ship_size_x):
        for j in range(y, y + ship_size_y):
            if not check_cell(field, i, j):
                return False
    
    return True


def spawn_ships(field: list, ship_collection: dict):
    for ship_size, ships_count in ship_collection.items():
        for i in range(ships_count):
            isVertical = randint(0,1) == 1
            
            if (isVertical):
                ship_size_x = 1
                ship_size_y = ship_size
            else:
                ship_size_x = ship_size
                ship_size_y = 1
            
            valid_cells = get_valid_cells(field, ship_size_x, ship_size_y)
            rand = randint(0, len(valid_cells) - 1)
            cell = valid_cells[rand]
            
            place_ship(field, cell[0], cell[1], ship_size_x, ship_size_y)


def shot(field: list, x: int, y: int):

    if field[y][x] == water:
        field[y][x] = miss
    elif field[y][x] == ship:
        field[y][x] = hit


def get_score(field):
    score = 0

    for field in field:
        for string in field:
            if hit in string:
                score += 1
    return score


def get_cells_for_shot(field: list):
    cells_for_shot = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] != miss or field[i][j] != hit:
                cells_for_shot.append((j, i))
    return cells_for_shot


def get_player_input():
    player_input = input("Enter coordinates to make a shot! To stop a game enter 'stop'.\n")
    lenght = len(player_input)

    if "stop" in player_input.lower():
        return False
    
    if (lenght > 3 or lenght < 1):
        print("Format of coordinates must be letter and number, f.e. a7")
        return get_player_input()
    
    char = player_input[0].upper()
    number = 0

    try:
        number = int(player_input[1:])
    except:
        print("Format of coordinates must be letter and number, f.e. a7")
        return get_player_input()

    if char not in letters:
        print("Format of coordinates must be letter and number, f.e. a7")
        return get_player_input()

    if number < 1 or number > size_y:
        print("Format of coordinates must be letter and number, f.e. a7")
        return get_player_input()

    return (number - 1, letters.index(char))


player_field = generate_array()
enemy_field = generate_array()

spawn_ships(player_field, ship_collection)
spawn_ships(enemy_field, ship_collection)


def play():
    max_score = sum([(ship * size) for ship, size in ship_collection.items()])
    
    while True:
        print_fields(player_field, enemy_field)
        player_input = get_player_input()

        if not player_input:
            print("The game was stopped! See you next time.")
            break
        
        shot(enemy_field, player_input[1], player_input[0])

        if get_score(enemy_field) == max_score:
            print("Congratulations! You won the game! русскій корабль пішов нахуй")
            break
        
        available_cells = get_cells_for_shot(player_field)
        index = randint(0, len(available_cells) - 1)
        cell = available_cells[index]
        
        shot(player_field, cell[0], cell[1])

        if get_score(player_field) == max_score:
            print("You lost. Better luck next time. русскій корабль енівей пішов нахуй")
            break


play()