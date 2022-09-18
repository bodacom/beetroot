# The Guessing Game.

# Write a program that generates a random number between 1 and 10 
# and lets the user guess what number was generated. 
# The result should be sent back to the user via a print statement.

import random

random_number = random.randint(0,10)

user_number = int(input('Please guess the number from 0 to 10:'))

# print(random_number, user_number)

if random_number == user_number:
    print('Yes, yes, exactly!')

else:
    print('Nope, it\'s not')

print('Random number = ', random_number)

print('Your number = ', user_number)