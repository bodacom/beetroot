# Task 2

# Write a function that takes in two numbers from the user via input(), 
# call the numbers a and b, and then returns the value of squared a divided by b, 
# construct a try-except block which raises an exception if the two values given 
# by the input function were not numbers, and if value b was zero (cannot divide by zero).    


def func():

    try:
        a = input('Please input a = ')
        b = input('Please input b = ')
        if a.isnumeric() and b.isnumeric():
            if not b == 0:
                return (a ** 2) / b
            else:
                raise ZeroDivisionError
        else:
            raise ValueError

    except ValueError:
        print('Error. Given \'a\' or \'b\' is not a number.')
        # raise ValueError

    except ZeroDivisionError:
        print("ZeroDivisionError. \'b\' can not be equal to 0")

    finally:
            if b == 0:
                print('b == 0')
                raise ZeroDivisionError

print(func())