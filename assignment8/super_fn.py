# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    
    def display(self):
        super().display()
        print(f"Subject: {self.subject}")


teacher1 = Teacher("Miss Horain Shah", "Mathematics")
teacher1.display()