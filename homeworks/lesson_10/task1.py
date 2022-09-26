# Task 1

# Write a function called oops that explicitly raises an IndexError exception when called. 
# Then write another function that calls oops inside a try/except state­ment to catch the error. 
# What happens if you change oops to raise KeyError instead of IndexError?

def oops():
    # raise IndexError
    raise KeyError


def catch():
    try:
        oops()
    except IndexError:
        print('An IndexError occured')
    except:
        print('other error occured')

catch()
