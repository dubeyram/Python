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
        print("Parent 1", self.name)


class Parent2:
    def __init__(self):
        self.name = "Parent2"

    def print_name(self):
        print("Parent2", self.name)


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
print(
    Child.__mro__
)  # to understand the order Python uses to resolve methods in inheritance.

"""
super() is used to call a method from the parent class (or superclass) without explicitly naming it.
"""


"""
More About Method Resolution Order (MRO)


If no super():
    MRO is used to find the first match → only one method executes.

If all use super() (cooperative):
    MRO determines the order in which all methods are executed,
    as each one hands off to the next.

"""


# MRO with super()
class A:
    def m(self):
        print("A")


class B(A):
    def m(self):
        print("B")
        super().m()


class C(A):
    def m(self):
        print("C")
        super().m()


class D(B, C):
    def m(self):
        print("D")
        super().m()


D().m()
print(D.__mro__)


# MRO without super()
class A:
    def show(self):
        print("A")


class B:
    def show(self):
        print("B")


class C(A, B):
    pass


C().show()
C.__mro__
