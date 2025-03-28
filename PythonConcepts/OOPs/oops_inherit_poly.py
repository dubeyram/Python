"""
This is a file that contains the code for the inheritance and polymorphism.
"""


class Animal:
    """
    This is a class that defines the animal.
    """

    def __init__(self, name) -> None:
        self.name = name

    def barks(self):
        """
        This is a method that defines the barks of the animal.
        """
        print(f"{self.name} barks")


class Dog(Animal):
    """
    This is a class that defines the dog.
    """

    def __init__(self, name, breed) -> None:
        super().__init__(name)
        self.breed = breed

    def barks(self):
        """
        This is a method that defines the barks of the dog.
        """
        super().barks()


dog = Dog("Buddy", "Golden Retriever")
dog.barks()
