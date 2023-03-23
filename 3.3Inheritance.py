# --------------------
# SECTION - III(c) - Extend a Class Functionality using Inheritance
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

        self.level = level

    def debug(self):
        print(f"{self.name} is debugging")

class Designer(Employee): # Syntax for a Child CLass
    
    def draw(self):
        print(f"{self.name} is drawing")

# Implementation of Child Class using the instance attributes and methods of Parent Class

se = SoftwareEngineer("Max", 24, 6000, "Junior")
print(se.name, se.age)
se.work()
print(se.level)

d = Designer("Phillip", 27, 7000)
print(d.name, d.age)
d.work()

se.debug()
d.draw()

# So this is How we "Extend" the Functionality of Base Class,
# using "draw" and "debug" named functions (as done above)

