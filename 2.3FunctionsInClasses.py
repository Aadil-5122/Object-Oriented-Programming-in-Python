# --------------------
# SECTION - II(c) - Functions with implementation using Decorators
# --------------------

# position, name, age, level, salary
se1 = ["software engineer", "Max", 20, "Junior", 5000]
se2 = ["software engineer", "Lisa", 25, "Senior", 7000]

# Function declaration outside the class

def code(se):
    print(f"{se[1]} is writing code")

code(se1)

# class (blueprint of data structure)

class SoftwareEngineer:

    alias = "Keyboard Magician"
    
    def __init__(self, name, age, level, salary):
        
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary 

    def code(self):
        print(f"{self.name} is writing code")

    # Parameterised Instance Method:

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    # Returnable Functions

    def information(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information

    def __str__(self) -> str:
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information

    def __eq__(self, other) -> str:
        return self.name == other.name and self.age == other.age
    
    # Functions without the "self" parameter
    # May be intentional / unintentional according to the programmer
    
    # If we try to call this function using an object of class by passing "age" (here) as a parameter,
    # the error which will pop in that: "one positional argument was required and two were given"
    # REASON: As told before, for every object, "self" is an automatically passed parameter,
    # Therefore the statement "se1.entry_salary(24)" is considered as "self.entry_salary(self, 24)",
    # but our function is defined to accept only one argument 

    # this will work if we call it using the class name: i.e.,
    # SoftwareEnginner.entry_salary(24)

    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000

# instance of class (object)
se1= SoftwareEngineer("Max", 20, "Junior", 5000)
se2= SoftwareEngineer("Lisa", 25, "Senior", 7000)
se3= SoftwareEngineer("Lisa", 25, "Senior", 7000)
print(se1.name, se1.age)

se1.code()
se2.code()

se1.code_in_language("Python")
se2.code_in_language("C++")

print(se1.information())

print(se1)

print(se2 == se3)

# entry_salary function called using the "Class Name"
# instead of object
print(SoftwareEngineer.entry_salary(27))

# So if we want to access an instance method which has no attribute "self",
# We use a "DECORATOR" named "@staticmethod", which allows us to call that function,
# with the help of an object of that class too

print(se1.entry_salary(24))

# But still we can't access the instance attributes,
# i.e., we still can't use "self.age" etc. in "entry_salary" function
 