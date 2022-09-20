# a = 10
# b = "4"

# try:
#     result = a/b
# except ZeroDivisionError:
#     print('Zero Division')

# except Exception as error:
#     print(f'Error {error}. You can not divide int by str')

# else:
#     print(f'All good. Your result {result}')

# finally:
#     print('All the time')

def func():
    try:
        a = 10
        b = -2

        if a < 0 or b < 0:
            raise ValueError("Numbers can't be lower 0")
    except ValueError:
        print("Numbers should be greater than zero.")
        return 0

    finally:
        return 1

print(func())