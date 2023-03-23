# --------------------
# SECTION - IV - Extension of Inheritance
# --------------------

# POLYMORPHISM:
# It alows us to write codes on Base Class, which can work on Child Classes as well.
# i.e., we can use a Child Class like its Parent, retaining Child Class's own Attributes.


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

# se = SoftwareEngineer("Max", 24, 6000, "Junior")
# print(se.name, se.age)
# print(se.level)

# d = Designer("Phillip", 27, 7000)
# print(d.name, d.age)

employees = [SoftwareEngineer("Max", 25, 6000, "Junior"),
             SoftwareEngineer("Lisa", 30, 9000, "Senior"),
             Designer("Phillip", 27, 7000)]


def motivate_employees(employees):
    for employee in employees:
        employee.work()


motivate_employees(employees)

# So, here we have used "work" function, 
# whose definition is different in each class,
# this is called Polymorphism
# Lines 51-61 shows the implementation of Polymorphism