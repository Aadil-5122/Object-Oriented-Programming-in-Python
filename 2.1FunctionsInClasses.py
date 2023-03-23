# --------------------
# SECTION - II(a)
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
    
    # So, the below declared is an instance method:

    # Here, in instance method as well, we need to make sure that the 1st parameter is "self"
    # This "self" keyword would allow the instance method to access all those instance attributes, 
    # which are declared in constructor    

    def code(self):
        print(f"{self.name} is writing code")

    # Parameterised Instance Method:

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}")

    # Returnable Functions

    def information(self):
        information = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information


# instance of class (object)
se1= SoftwareEngineer("Max", 20, "Junior", 5000)
se2= SoftwareEngineer("Lisa", 25, "Senior", 7000)
print(se1.name, se1.age)


# Calling Instance Method using Instance of Class
se1.code()
se2.code()

# Calling the Parameterised Instance Method
se1.code_in_language("Python")
se2.code_in_language("C++")

# Calling the Instance method which return information too
print(se1.information())

# Note: We do not pass "self" as a parameter while calling instance method or constructor,
# it is because it is already included for us as a 1st parameter.

# So basically the self object specifies the instance of a particul.ar object.



