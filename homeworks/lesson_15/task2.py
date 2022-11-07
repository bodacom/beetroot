# Task 2

# Doggy age

# Create a class Dog with class attribute `age_factor` equals to 7. 
# Make __init__() which takes values for a dog’s age. 
# Then create a method `human_age` which returns the dog’s age in human equivalent.


class Dog:

    age_factor = 7

    def __init__(self, dogs_age) -> None:
        self.age = dogs_age

    def humans_age(self):
        return self.age * Dog.age_factor


dog = Dog(7)

print(dog.humans_age())