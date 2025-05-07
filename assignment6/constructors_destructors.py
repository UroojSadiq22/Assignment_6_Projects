# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


class Logger:
    def __init__(self, name):
        self.name = name
        print(f"Logger {self.name} created.")

    def __del__(self):
        print(f"Logger {self.name} destroyed.")


logger1 = Logger("Logger1")
logger2 = Logger("Logger2")

print("Performing some operations...")

del logger1
del logger2
