# --------------------
# SECTION - I - Classes and Objects
# --------------------


# position, name, age, level, salary
se1 = ["software engineer", "Max", 20, "Junior", 5000]
se2 = ["software engineer", "Lisa", 25, "Senior", 7000]

# class (blueprint of data structure)

class SoftwareEngineer:

    # Class Attributes

    alias = "Keyboard Magician"
    
    # Special function to initialise our object (Constructor)
    # Herein, self attribute will always be there 
    def __init__(self, name, age, level, salary):

        # So the below mentioned attributes with a self keyword,
        # are known as instance attributes and can be used inside the class.
        # the attributes defined outside this function are called Class Attributes.
        
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


# Difference between Instance and Class Attributes:

# Instance Attributes belong to a specific object and not to the whole Class
# i.e., we can write: se1.alias, SoftwareEnginner.alias 
# but not : SoftwareEngineer.name

# instance of class (object)
se1= SoftwareEngineer("Max", 20, "Junior", 5000)
print(se1.name, se1.age)




