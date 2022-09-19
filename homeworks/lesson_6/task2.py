# Task 2

# Exclusive common numbers.

# Generate 2 lists with the length of 10 with random integers from 1 to 10, 
# and make a third list containing the common integers between the 2 initial lists without any duplicates.

# Constraints: use only while loop and random module to generate numbers

import random

list_1 = []
list_2 = []

while len(list_1) < 10:
    list_1.append(random.randint(1, 10))
    list_2.append(random.randint(1, 10))

# print(len(list_1), len(list_2))

list_common = list(set(list_1) & set(list_2))

print(list_1)
print(list_2)
print(list_common)