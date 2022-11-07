# Task 1

# School

# Make a class structure in python representing people at school. 
# Make a base class called Person, a class called Student, and another one called Teacher. 
# Try to find as many methods and attributes as you can which belong to different classes,
# and keep in mind which are common and which are not. For example, the name should be 
# a Person attribute, while salary should only be available to the teacher. 

class Pesron:
    def __init__(self, 
                 first, 
                 last, 
                 age, 
                 sex, 
                 weight, 
                 height, 
                 skin, 
                 eyes_color, 
                 hair_color, 
                 birthday
                ) -> None:
        self.first_name = first
        self.last_name = last
        self.age = age
        self.sex = sex
        self.weight = weight
        self.height = height
        self.skin = skin
        self.eyes_color = eyes_color
        self.hair_color = hair_color
        self.birth_date = birthday


class Student(Pesron):
    def __init__(self, grade, subjects, schedule, marks, sport, father, mother) -> None:
        self.grade
        self.subjects
        self.schedule
        self.marks
        self.sport
        self.father
        self.mother


class Teacher(Pesron):
    def __init__(self, subjects, schedule, salary) -> None:
        self.subjects = subjects
        self.schedule = schedule
        self.salary = salary


