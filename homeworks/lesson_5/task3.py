# Words combination

# Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.

# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters 

# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …

# Tips: Use random module to get random char from string)


import random


input_string = input("Provide an input string, please: ")

for string_number in range(0, 5):
    print(string_number + 1, end=') ')
    for position in input_string:
        print(input_string[random.randint(0, len(input_string)-1)], end='')
    print()
