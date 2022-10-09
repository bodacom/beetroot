# Task 3

# Write a decorator `arg_rules` that validates arguments passed to the function.

# A decorator should take 3 arguments:

# max_length: 15

# type_: str

# contains: [] - list of symbols that an argument should contain

# If some of the rules' checks returns False, the function should return False and print the reason it failed
# otherwise, return the result.

# ```


# def arg_rules(type_: type, max_length: int, contains: list):

#     pass


# @arg_rules(type_=str, max_length=15, contains=['05', '@'])
# def create_slogan(name: str) -> str:

#     return f"{name} drinks pepsi in his brand new BMW!"


# assert create_slogan('johndoe05@gmail.com') is False

# assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

# ```


def arg_rules(type_: type, max_length: int, contains: list):
    def get_func(func):
        def wrapper(*args, **kwargs):
            result = func()
            return 

        return wrapper
    return get_func


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:

    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
