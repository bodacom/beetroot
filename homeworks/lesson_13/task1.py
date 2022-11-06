# Task 1

# Write a Python program to detect the number of local variables declared in a function.

def test_function():
    a = None
    b = None
    c = None

    return None

print(test_function.__code__.co_nlocals)