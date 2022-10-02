def uppercase(func):
    def upper(*args, **kw):
        result = func()
        return result.upper()
    return upper


def bold(func):
    def wrapper(*args, **kwargs):
        result = func()
        result = '<b>' + result + '</b>'
        return result
    return wrapper


@uppercase
def ukraine_greeting():
    return "Слава Україні!"

print(ukraine_greeting())

@bold
def ukraine_greeting():
    return "Слава Україні!"

print(ukraine_greeting())