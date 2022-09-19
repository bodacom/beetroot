# Task 3

# A simple calculator.

# Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter 
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second parameter. 
# Then return the sum or product of all the numbers in the arbitrary parameter. For example:

#     the call make_operation(‘+’, 7, 7, 2) should return 16
#     the call make_operation(‘-’, 5, 5, -10, -20) should return 30
#     the call make_operation(‘*’, 7, 6) should return 42  


def make_operation(operation, *args):
    
    if operation == "+":
        result = 0
        for arg in args:
            result += arg
    elif operation == "-":
        result = 0
        for arg in args:
            result -= arg
    elif operation == "*":
        result = 1
        for arg in args:
            result *= arg

    return result


# print(make_operation('*', 2, 3, 4))
