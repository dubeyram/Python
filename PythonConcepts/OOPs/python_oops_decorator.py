"""
Python OOP, there are several powerful decorators commonly used to manage attributes and methods. 
These help you control how class properties behave, and improve encapsulation, readability, and maintainability.
"""

"""
-----------------------------------------------property decorator-----------------------------------------------

Allows to access a method like an attribute.
Useful for read-only attributes or computed properties.
"""


class Employee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


emp = Employee("John")
print(emp.name)


"""
-----------------------------------------------@<property_name>.setter decorater-----------------------------------------------
Makes the @property writable.
Controls how the attribute is set, allowing validation or transformation.
"""


class Employee:
    def __init__(self, name, age=35):
        self._name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if len(new_name) < 5:
            raise ValueError("Name too short")
        self._name = new_name


emp = Employee("n")
emp.name = "Testing"  # Return error 'Name too short'
print(emp.name)
print(emp.age)


"""
-----------------------------------------------@<property_name>.deleter decorator -----------------------------------------------
Allows deleting a property with del keyword.

"""


class Employee:
    def __init__(self, name, age=35):
        self._name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.deleter
    def name(self):
        print("Deleting name...")
        del self._name


emp = Employee("Testing Deleter")
del emp.name
try:
    print(emp._name)
except Exception as e:
    print(str(e))  #'Employee' object has no attribute '_name'


"""
-----------------------------------------------@<property_name>.staticmethod decorator -----------------------------------------------
Used when the method does not use self or cls.

Utility/helper methods related to the class.
"""


class Math:
    @staticmethod
    def add(x, y):
        return x + y


print(Math.add(5, 7))


"""
-----------------------------------------------@<property_name>.classmethod decorator -----------------------------------------------
Used when method needs access to the class (cls) not the instance.

Often used as alternative constructors or factory methods.
"""


class Person:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, data):
        name = data.split("-")[0]
        return cls(name)


p = Person.from_string("Ram-28-India")
print(p.name)


"""
-----------------------------------------------@abstractmethod decorator -----------------------------------------------
Used to create abstract base classes.

Forces subclasses to implement the method.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Woof")


"""
-----------------------------------------------Custom Decorators (Advanced OOP usage) -----------------------------------------------
Define own decorators to enforce rules like logging, permission checks, timing, etc.
"""


def log_method(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


class Demo:
    @log_method
    def hello(self):
        print("Hello!")


Demo().hello()
