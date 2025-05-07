# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Department:
    def __init__(self, name):
        self.name = name

    def get_department_name(self):
        return self.name

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department  # Aggregation: Employee has a reference to Department

    def get_employee_info(self):
        return f"Employee Name: {self.name}, Department: {self.department.get_department_name()}"


e1 = Employee("Urooj Sadiq", Department("HR"))
e2 = Employee("Fatima Khan", Department("Finance"))
e3 = Employee("Ali Ahmed", Department("IT"))
e4 = Employee("Sara Ali", Department("Marketing"))


print(e1.get_employee_info())