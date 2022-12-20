# Task 1

# Method overloading.

# Create a base class named Animal with a method called talk and then create two subclasses: 
# Dog and Cat, and make their own implementation of the method talk be different. 
# For instance, Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.

# Also, create a simple generic function, which takes as input instance of a Cat or Dog classes and performs talk method on input parameter.  


class Animal:

    def __init__(self, animal) -> None:
        self.animal = animal

    def talk(self):
        return 'Hi'


class Dog(Animal):

    def talk(self):
        return 'woof woof'


class Cat(Animal):

    def talk(self):
        return 'meow'


def animal_talks(instance):
    return instance.talk()


a = Animal('Horse')
d = Dog('Mike')
c = Cat('Black')

animals = [a, d, c]

for animal in animals:
    print(animal_talks(animal))
