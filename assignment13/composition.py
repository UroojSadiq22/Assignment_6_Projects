# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return f"{self.horsepower} HP engine"

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine

    def start(self):
        return f"{self.brand} is going to start with {self.engine.start()}!"


engine = Engine(150)
car = Car("Toyota", engine)
print(car.start()) 