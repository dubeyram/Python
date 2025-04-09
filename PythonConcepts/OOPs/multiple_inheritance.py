"""
Multiple Inheritance (MI):

When a child class inherits attributes and methods from multiple parent classes, 
the child class inherits all the attributes and methods of the parent classes.

----------------------------------------Example for Multiple Inheritance----------------------------------------

Method Resolution Order (MRO):

When multiple parents have same method name, python used the Method Resolution Order to decide which one to call.

"""

class Parent1:
    def __init__(self):
        self.name = "Parent1"

    def print_name(self):
        print("Parent 1",self.name)


class Parent2:
    def __init__(self):
        self.name = "Parent2"

    def print_name(self):
        print("Parent2",self.name)


class Child(Parent1, Parent2):
    def __init__(self):
        super().__init__()
        self.name = "Child"

    # def print_name(self):
    #     print(self.name)


if __name__ == "__main__":
    child = Child()
    child.print_name()



"""
----------------------------------------Example for Multilevel Inheritance----------------------------------------

Inheritance that forns a chain -- a class inherits from a class, which itself inherited another class

"""

class Grandfather:
    def __str__(self) -> str:
        print("Class Grandfather")
        return "Class GrandFather"

class Father(Grandfather):
    def __str__(self) -> str:
        print("Class Father")
        return super().__str__()
    
class Child(Father, Grandfather):
    def __str__(self) -> str:
        print("Child Class")
        return super().__str__()

child = Child()
print(child)
print(Child.__mro__) # to understand the order Python uses to resolve methods in inheritance.

"""
super() is used to call a method from the parent class (or superclass) without explicitly naming it.
"""