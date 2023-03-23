# --------------------
# SECTION - V(a) - Private Instance Variables
# --------------------

# ENCAPSULATION: Hiding of Data Implementation, For exanple, the instance variables 
# are kept hidden and there is only one Access Method outside, which can Manipulate these Variables.

# Instance methods can also be kept private so that they can be used, Only INTERNALLY

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # We declare Private Instance Variables starting with "_"
        # To initialise them, we use a Function and not the default Constructor
        self._salary = None # Private Instance Variable
        self.__salary1 = None
        self._num_bugs_resolved = 0 # Private Instance Variable

    # Also called "Getter" Function

    def get_salary(self):
        return self._salary
    
    # Also called "Setter" Function

    def set_salary(self, value):
        self._salary = value

    # Ideally, these two above Functions should be the only Functions who can access,
    # Private Instance Variables

    # Application Of Getter and Setter Functions:
    # Checking of Value, Enforcing Constraints etc.

se = SoftwareEngineer("Max", 25)
print(se.age, se.name, se._salary)

# As Line 23 easily accessed "_salary", therefore in Python the variable with "_",
# is not actually Private,

# To make a variable actually Private, we preceed a variable with "__",
# i.e. "double under-score"

# STRICTLY SPEAKING:
# "_x" is called "PROTECTED" attribute
# "__x" is called "PRIVATE" attribute

se.set_salary(6000)
print(se.get_salary())