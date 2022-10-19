# Розбирати записи на складові
# Словник із групуванням на:
#     проекти (задачі, ще щось)
#     програми
#     назви файлів
#     час використання: кожна секунда в трекінгу відповідає секунді використання.
#     час простою: не вважати використанням, якщо немає активності миші більше хх секунд?

import time
import datetime



def read_log(log_file_name: str = 'tracker_log.txt') -> list:
    '''
    Reads all the file content.
    Returns list containing lines.
    '''
    
    with open(log_file_name, 'r') as log_file:
        log_dump = log_file.readlines()
    print(f'Довжина файла {len(log_dump)} стрічок')
    
    return log_dump


def make_entities(log_dump: list) -> list:
    '''
    Makes entities from raw log_dump str list.
    Returns list with entities of list type.
    '''
    log_entities = []
    entity = []
    
    for line in log_dump:
        # if line_counter == 4:
        #     log_entities.append(entity)
        #     entity = []
        #     line_counter = 1
        # else:
        #     entity.append(line.rstrip())
        #     line_counter += 1
        try:
            float(line)
            if len(entity) !=0:
                log_entities.append(entity)
                entity = []
            entity.append(line.rstrip())
        except:
            entity.append(line.rstrip())

    del entity
    print('Кількість записів = ', len(log_entities))
    
    return log_entities


def unique_names(log_entities: list) -> list:
    '''
    Defines unique names of windows loged.
    Returns a list with unique names as strings.
    '''
    entities_names = []
    for entity in log_entities:
        entities_names.append(entity[1])
        
    uniq_names = list(set(entities_names))
    print('Number of unique names: ',len(uniq_names))

    return uniq_names


def sorted_frequency_dictionary(entities: list, reversed: bool = True) -> dict:
    '''
    Sorts names by times of appearance.
    Returns a dictionary of unique names as keys and frequency as values
    '''
    frequency_dictionary = {}
    # define names frequency:
    for entity in entities:
        if frequency_dictionary.get(entity[1]):
            frequency_dictionary[entity[1]] += 1
        else:
            frequency_dictionary[entity[1]] = 1

    frequency_dictionary = {k: v for k, v in sorted(frequency_dictionary.items(), key=lambda item: item[1], reverse=reversed)}

    return frequency_dictionary


lines = read_log()
log_entities = make_entities(lines)

frequency_dictionary = sorted_frequency_dictionary(log_entities, False)

# for entity in log_entities:
#     # if entity[1] == '':
#     #     print(datetime.datetime.utcfromtimestamp(float(entity[0])).strftime('%Y-%m-%d %H:%M:%S'))
#     try:
#         float(entity[0])
#         if entity[1] == '':
#             print(datetime.datetime.utcfromtimestamp(float(entity[0])).strftime('%Y-%m-%d %H:%M:%S'))
#     except Exception:
#         print(entity)

total = 0
telegram_time = 0
mozilla_time = 0
for key, value in frequency_dictionary.items():
    print(str(datetime.timedelta(seconds = value)), key)
    total += value
    if 'Telegram' in key:
        telegram_time += value
    if 'Mozilla' in key:
        
        mozilla_time += value

print(str(datetime.timedelta(seconds = telegram_time)), 'Total telegram time')
print(str(datetime.timedelta(seconds = mozilla_time)), 'Total mozilla time')
print(str(datetime.timedelta(seconds = total)), 'Total time')
print('Tracking started: ', time.ctime(float(log_entities[0][0])))
print('Last entity: ', time.ctime(float(log_entities[-1][0])))



# print(type(log_lines))
# print(type(log_lines[0]))
# print(log_lines[0])

# for index in range(10):
#     print(log_lines[index])
