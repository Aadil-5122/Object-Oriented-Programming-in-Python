# --------------------
# SECTION - II(b) - Some Special Instance Methods
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
    
    # SOME SPECIAL METHODS:

    # These are called "Double Underscore" OR "d underscoore" Methods
    # They start with a leading "double underscore" and end with a "trailing double underscore", Ex. "init" function used before
    # They are already provided for us in Python
    # Every object already has them, So,
    # even if we do not declare them in our program, we can use them for any object in the program, because,
    # every object already contains implementation of such functions

    # if we have defined our own "d underscore function", then that will be implemented instead of what already object has

    # The below function will get executed whenever our object will get converted to string
    # i.e., if we try to print an object, instead of it displaying the the class of that object and 
    # the object's memory location, it will implement "__str__" function

    def __str__(self) -> str:
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information

    # we can clearly see that the above function can be used instead of,
    # our previouslt defined function named "information"

    # ANOTHER Special Function: "__eq__"
    # It has two mandatory parameters: "self" and "other"
    # This is used for comparing two objects
    # By Default (i.e. if we do not declare it in our program),
    # It will compare the memory addresses of both the objects 

    def __eq__(self, other) -> str:
        return self.name == other.name and self.age == other.age

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

# To print "class" and "memory location" of an object (if "__str__" is not declared in our program)
print(se1)
# else it will implement "__str__" function

# To compare memory adresses of two objects and return True/False (if "__eq__" is not declared in our program)
print(se2 == se3)



