# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result1 = MathUtils.add(5, 10)
print("Sum of 5 and 10 is:", result1)

result2 = MathUtils.add(20, 30)
print("Sum of 20 and 30 is:", result2)