# --------------------
# SECTION - V(b) - Private Instance Methods
# --------------------

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age

        self._salary = None # Private Instance Variable
        self.__salary1 = None # Private Instance Variable
        self._num_bugs_resolved = 0 # Private Instance Variable

    def code(self):
        self._num_bugs_resolved += 1

    # Also called "Getter" Function

    def get_salary(self):
        return self._salary
    
    # Also called "Setter" Function

    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)

    # the names of Private Instance Methods also start with "_"

    def _calculate_salary(self, base_value):
        if self._num_bugs_resolved < 10:
            return base_value
        if self._num_bugs_resolved < 100:
            return base_value * 2
        return base_value * 3
    
    # So basically the above method which involves the calculation, remains hidden,
    # and the user basically has access to getter and setter functions.

se = SoftwareEngineer("Max", 25)
print(se.age, se.name, se._salary)

for i in range(70):
    se.code()

se.set_salary(6000)
print(se.get_salary())

