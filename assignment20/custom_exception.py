# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or older.")
    else:
        return "Age is valid."

class InvalidAgeError(Exception):
    pass

try:
    print(check_age(16))
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")
finally:
    print("Age check completed.")