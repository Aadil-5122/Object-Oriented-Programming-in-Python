# --------------------
# SECTION - III(b) - OverRide a Class Function using Inheritance
# --------------------

class Employee: # Parent Class
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f'{self.name} is working')


class SoftwareEngineer(Employee): # Syntax for a Child Class
    
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)

        # As this class already has the initialiser function of its Parent Class,
        # So to initialise the already existing attributes, we call the Initialser of Parent Class,
        # using the above statement "super().__init__(name, age)"

        self.level = level

        # So basically the above attribute "level" only works for SoftwareEngineer,
        # and not the Designer

class Designer(Employee): # Syntax for a Child CLass
    pass

# Implementation of Child Class using the instance attributes and methods of Parent Class

se = SoftwareEngineer("Max", 24, 6000, "Junior")
print(se.name, se.age)
se.work()
print(se.level)

d = Designer("Phillip", 27, 7000)
print(d.name, d.age)
d.work()

# Basically what we have done above is,
# We have "over-ridden" the Parent Class Initialiser Function for a SoftWare Engineer,
# Note that it is mandatory to use "super().__init__()" for correct initialisation of the object.
# Application: We wanted to define "level" for a Software Engineer but not the Designer
