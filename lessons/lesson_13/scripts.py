# # Example 1 from video 1

# def add_five(x):
#     return x + 5


# def do_twice(f):
#     def resulting_func(x):
#         return f(f(x))
#     return resulting_func


# result = do_twice(add_five)
# print(result(5))


# Example 2 from video 1

import math


def make_cylinder_volume_function(r: int):
    def volume(h: int) -> float:
        return math.pi * r**2 * h
    return volume


volume_r10 = make_cylinder_volume_function(10)
print(volume_r10(30)/(30*100))


