# --------------------
# SECTION - VI(a) - Properties
# --------------------

# Now, we will write Getter and Setter Functions in more "Pythonic" way!
# i.e. we will use Decorators in Python 

class SoftwareEngineer:

    def __init__(self):

        self._salary = None # Private Instance Variable

    # def get_salary(self):
    #     return self._salary

    @property
    def salary(self):
        return self._salary
    
    # def set_salary(self, value):
    #     self._salary = value

    @salary.setter
    def salary(self, value):
        self._salary = value

    # i.e. instead of conventional way of writing Getter and Setter Functions, (as in the commented 4 lines)
    # we write it using Decorators: wherein,
    # Getter and Setter Function get the same name as the property for which they are getter and setter (here salary)

    # Decorator of Getter is the built-in Decorator: "@property"
    # Decorator of Setter is also built-in but written using Property name as: "@salary.setter"


    # General Example of another Decorator pertaining to this topic:

    @salary.deleter
    def salary(self):
        del self._salary

se = SoftwareEngineer()

# se.set_salary(6000)
# print(se.get_salary())

se.salary = 6000
print(se.salary)

# Here too the Getter and Setter Functions are called in the way as mentioned in the above two lines

del se.salary # to run the third of the above mentioned function

# the above statement will delete the instance varibale,
# so printing anything pertaining to this variable would throw an error

