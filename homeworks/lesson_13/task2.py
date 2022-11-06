# Task 2

# Write a Python program to access a function inside a function 
# (Tips: use function, which returns another function)

def function_external():
    def function_internal():
        input('Press enter')
        return 'Done inside'
    return function_internal

variable_external = function_external
variable_internal = variable_external()

print(variable_internal())