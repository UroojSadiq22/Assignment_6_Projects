# Assignment:
# Create a class Employee with:

# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public variable
        self._salary = salary  # Protected variable
        self.__ssn = ssn  # Private variable

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}")


employee1 = Employee("Urooj Sadiq", 50000, "123-45-6789")
print("Accessing public variable:", employee1.name)  # Accessible
print("Accessing protected variable:", employee1._salary)  # Accessible but should be treated as protected
print("Accessing private variable:", employee1._Employee__ssn)  # Accessible using name mangling

employee1.display_info()  # Accessing all variables through a method

