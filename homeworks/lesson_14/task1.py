# Task 1

# Write a decorator that prints a function with arguments passed to it.

# NOTE! It should print the function, not the result of its execution!

# For example:

#  "add called with 4, 5"

# ```


# def logger(func):

#     pass


# @logger
# def add(x, y):

#     return x + y


# @logger
# def square_all(*args):

#     return [arg ** 2 for arg in args]


# ```


def logger(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__}() called with', end='')
        if len(args) > 0:
            for index, arg in enumerate(args):
                if index + 1 != len(args):
                    print(f' {arg},', end='')
                else:
                    print(f' {arg}', end='')
        else:
            print(' no positional arguments')
        if len(kwargs.keys()) > 0:
            print(' and', end='')
            for key, argument in kwargs.items():
                print(f' {key}=\'{argument}\',', end='')
            print()
        else:
            print(' and no keyword arguments')
    return wrapper



@logger
def add(x, y, *args, **kwargs):

    return x + y


@logger
def square_all(*args):

    return [arg ** 2 for arg in args]

add(1, 2, 3, 4, boda='name')

square_all(2, 3, 4)
