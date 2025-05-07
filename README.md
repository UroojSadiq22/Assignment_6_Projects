# Python OOP Concepts - Assignment Collection

This repository demonstrates 21 core Object-Oriented Programming (OOP) and Python concepts using clear, beginner-friendly examples. Each concept is represented by a dedicated assignment for better understanding and practical implementation.

---

## 📋 Assignments Overview

### 1. **Using `self`**
- **Concept:** Instance variables and constructor.
- **Task:** Create a `Student` class with `name` and `marks`, and display them using `self`.

### 2. **Using `cls`**
- **Concept:** Class variables and class methods.
- **Task:** Create a `Counter` class that tracks how many instances have been created using a class variable and method.

### 3. **Public Variables and Methods**
- **Concept:** Access modifiers.
- **Task:** Create a `Car` class with a public `brand` and `start()` method. Access both outside the class.

### 4. **Class Variables and Class Methods**
- **Concept:** Shared data across instances.
- **Task:** Create a `Bank` class with a class variable `bank_name`. Add a class method to change it.

### 5. **Static Variables and Static Methods**
- **Concept:** Methods that do not depend on class or instance variables.
- **Task:** Create `MathUtils` class with a static method `add(a, b)`.

### 6. **Constructors and Destructors**
- **Concept:** Object lifecycle.
- **Task:** Create a `Logger` class that prints messages on creation and destruction of an object.

### 7. **Access Modifiers: Public, Protected, and Private**
- **Concept:** Data protection and encapsulation.
- **Task:** Create an `Employee` class with public, protected, and private variables. Try accessing them from outside.

### 8. **The `super()` Function**
- **Concept:** Inheritance and constructor chaining.
- **Task:** Create a `Person` and a derived `Teacher` class. Use `super()` to call the parent constructor.

### 9. **Abstract Classes and Methods**
- **Concept:** Interface enforcement using `abc` module.
- **Task:** Create abstract class `Shape` with an abstract method `area()`. Implement it in `Rectangle`.

### 10. **Instance Methods**
- **Concept:** Working with instance-specific data.
- **Task:** Create a `Dog` class with a method `bark()` that uses instance variables.

### 11. **Class Methods**
- **Concept:** Operating on class-level data.
- **Task:** Create a `Book` class with a class variable and class method to track total books.

### 12. **Static Methods**
- **Concept:** Utility-like behavior within classes.
- **Task:** Create `TemperatureConverter` class with a static method `celsius_to_fahrenheit(c)`.

### 13. **Composition**
- **Concept:** "Has-a" relationship between classes.
- **Task:** Pass an `Engine` object into a `Car` object and use it internally.

### 14. **Aggregation**
- **Concept:** Weaker "has-a" relationship where objects exist independently.
- **Task:** `Department` stores a reference to an independent `Employee` object.

### 15. **Method Resolution Order (MRO) and Diamond Inheritance**
- **Concept:** How Python resolves method calls in multiple inheritance.
- **Task:** Create classes `A`, `B`, `C`, and `D` with overridden `show()` methods. Call `show()` on an object of `D`.

### 16. **Function Decorators**
- **Concept:** Add functionality before/after a function runs.
- **Task:** Create `log_function_call` decorator to log a message before `say_hello()` runs.

### 17. **Class Decorators**
- **Concept:** Modify or extend classes dynamically.
- **Task:** Create `add_greeting` class decorator that adds a `greet()` method to `Person`.

### 18. **Property Decorators**
- **Concept:** Controlled access to attributes using `@property`, `@setter`, and `@deleter`.
- **Task:** Manage a `_price` attribute in `Product` class with getter, setter, and deleter.

### 19. **callable() and `__call__()`**
- **Concept:** Make objects behave like functions.
- **Task:** Create `Multiplier` class that can be called like a function to multiply a number.

### 20. **Creating a Custom Exception**
- **Concept:** Raising and handling custom errors.
- **Task:** Create `InvalidAgeError` and raise it in `check_age()` if age < 18.

### 21. **Making a Custom Class Iterable**
- **Concept:** Implementing `__iter__()` and `__next__()` to make objects iterable.
- **Task:** Create `Countdown` class that counts down from a start number in a for-loop.

---

## 🔧 Requirements

- Python 3.x
- No third-party libraries required

---

## 📦 How to Run

Clone the repository and run any assignment file:
```bash
python <filename>
