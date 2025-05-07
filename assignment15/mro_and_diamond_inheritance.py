# Assignment:
# Create four classes:

# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        return "I am in class A"

class B(A):
    def show(self):
        return "I am in class B"

class C(A):
    def show(self):
        return "I am in class C"

class D(C, B):
    pass


d = D()
print(d.show())  
