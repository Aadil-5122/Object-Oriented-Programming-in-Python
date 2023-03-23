# --------------------
# SECTION - III(a) - Inheritance
# --------------------

# Process in which one class takes in attributes and methods of one class,
# So, this newly formed class is then called "Child Class" and
# Other one is called "Parent Class"

# Using Inheritance, we can: 
# 1. Inherit a Class
# 2. Extend a Class
# 3. OverRide a Class

class Employee: # Parent Class
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # Now both the Child Classes have the above instance attributes,
        # i.e., the "age" and the "name"

    # Same goes for Instance Methods,
    # i.e., Child Class Inherits Instance Methods as well

    def work(self):
        print(f'{self.name} is working')


class SoftwareEngineer(Employee): # Syntax for a Child Class
    pass

class Designer(Employee): # Syntax for a Child CLass
    pass

# Implementation of Child Class using the instance attributes and methods of Parent Class

se = SoftwareEngineer("Max", 24)
print(se.name, se.age)
se.work()

d = Designer("Phillip", 27)
print(d.name, d.age)
d.work()