# Task 1

# The greatest number

# Write a Python program to get the largest number from a list of random numbers with the length of 10

# Constraints: use only while loop and random module to generate numbers

import random

list_of_numbers = []
i = 0

while i<10:
    list_of_numbers.append(random.randint(-100, 100))
    i += 1

print(str(len(list_of_numbers)) + ':', list_of_numbers)
print(max(list_of_numbers))
