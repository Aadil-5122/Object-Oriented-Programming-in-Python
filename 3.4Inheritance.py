# --------------------
# SECTION - III(d) - OverRide a Class Function using Inheritance
# --------------------

# So in simple words, if we CREATE a NEW Function in Child Class:
# (a) with same name as in Base Class -> "Over-Riding"
# (b) with name not in Base Class -> "Extending"

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

    def work(self):
        print(f'{self.name} is coding')

class Designer(Employee): # Syntax for a Child CLass
    
    def draw(self):
        print(f"{self.name} is drawing")

    def work(self):
        print(f'{self.name} is designing')

# Implementation of Child Class using the instance attributes and methods of Parent Class

se = SoftwareEngineer("Max", 24, 6000, "Junior")
print(se.name, se.age)
print(se.level)

d = Designer("Phillip", 27, 7000)
print(d.name, d.age)

se.work()
d.work()

# As per the Output of Lines 50 and 51,
# We can clearly see that when "work" function is called, 
# Both the Child Classes Implement their own "work" function,
# instaed of calling "work" function defined in the Base Class
