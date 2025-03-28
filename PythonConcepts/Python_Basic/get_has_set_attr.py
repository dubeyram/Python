"""
This is a file that contains the code for the get, has and set attributes.
"""


class Person:
    """
    This is a class that contains the person's name and age.
    """

    def __init__(self, name, age):
        """
        This is the constructor of the class.
        """
        self.name = name
        self.age = age


p = Person("Alice", 25)

# Using hasattr() to check if an attribute exists
if hasattr(p, "age"):
    print(f"Age exists: {getattr(p, 'age')}")  # Using getattr() to get the value

# Using getattr() with a default value for a non-existent attribute
print(f"Gender: {getattr(p, 'gender', 'Not specified')}")  # Output: Not specified

# Using setattr() to dynamically add a new attribute
setattr(p, "gender", "Female")
print(f"Newly added gender: {p.gender}")  # Output: Female

# Using setattr() to modify an existing attribute
setattr(p, "age", 30)
print(f"Updated age: {p.age}")  # Output: 30
