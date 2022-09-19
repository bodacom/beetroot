# Task 4

#     Створити лист із днями тижня.
#     В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
#     Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

dict_days = dict([(i+1, days_of_week[i]) for i in range(len(days_of_week))])

print(dict_days)

days_dict = {}

for index, day in enumerate(days_of_week):
    days_dict[day] = index + 1

print(days_dict)