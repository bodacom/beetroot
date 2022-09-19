# Task 3

# Extracting numbers.

# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, 
# and store them in a separate list. Finally, print the list.

# Constraint: use only while loop for iteration


list_of_integers = list(range(1, 101))

i = 0
list_len = len(list_of_integers)
separation_list = list()

while i < list_len:

    if list_of_integers[i] % 7 == 0 and list_of_integers[i] % 5 != 0:
        separation_list.append(list_of_integers[i])

    i += 1

print(separation_list)