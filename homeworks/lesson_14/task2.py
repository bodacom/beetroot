# Task 2

# Write a decorator that takes a list of stop words and replaces them 
# with * inside the decorated function

# ```


# def stop_words(words: list):

#     pass


# @stop_words(['pepsi', 'BMW'])
# def create_slogan(name: str) -> str:

#     return f"{name} drinks pepsi in his brand new BMW!"


# assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

# ```



def stop_words(words: list):
    def someth(func):
        def wrapper(*args, **kwargs):
            result = func(args[0])
            for word in words:
                result = result.replace(word, '*')
            return result
        return wrapper
    return someth



@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

try:
    assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
    print('All good.')
except AssertionError:
    print('Unexpected behavior')
