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
            if not int(b) == 0:
                return (int(a) ** 2) / int(b)
            else:
                raise ZeroDivisionError
        else:
            raise ValueError

    except ValueError:
        print('Error. Given \'a\' or \'b\' is not a number.')
        try:
            if int(b) == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("ZeroDivisionError. \'b\' can not be equal to 0")
    except ZeroDivisionError:
        print("ZeroDivisionError. \'b\' can not be equal to 0")


print(func())