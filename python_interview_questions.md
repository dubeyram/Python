1.Mutable vs Immutable Types
- Mutable types can be changed after they are created (e.g., lists, dictionaries).
- Immutable types cannot be changed once created (e.g., strings, tuples).

2. **Shallow vs Deep Copy**
- A shallow copy creates a new object but inserts references into it to the objects found in the original.
- A deep copy creates a new object and recursively adds copies of nested objects found in the original.

3. **Decorators**
- Decorators are functions that modify the behavior of other functions or methods. They are often used for logging, access control, and instrumentation.

4. **Generators**
- Generators are a type of iterable that generate values on the fly and use the `yield` statement to produce a series of values over time, saving memory.

5. **List Comprehensions vs Generator Expressions** 
- List comprehensions create a full list in memory, while generator expressions produce items one at a time and are more memory efficient.

6. **Lambda Functions**
- Lambda functions are small anonymous functions defined with the `lambda` keyword, often used for short, throwaway functions.
- Example: `lambda x: x + 10` creates a function that adds 10 to its input.

7. **Filter, Map, and Reduce**
- `filter()` applies a function to each item in an iterable and returns only those items for which the function returns True.
- `map()` applies a function to each item in an iterable and returns a new iterable with the results.
- `reduce()` (from the `functools` module) applies a binary function cumulatively to the items of an iterable, reducing it to a single value.

8. **args vs kwargs**
- `*args` allows a function to accept a variable number of positional arguments.
- `**kwargs` allows a function to accept a variable number of keyword arguments.

9. **Set vs Frozenset**
- A set is a mutable collection of unique elements, allowing addition and removal of items.
- A frozenset is an immutable version of a set, meaning its elements cannot be changed after creation.

10. **Context Managers**
- Context managers are used to manage resources, ensuring proper acquisition and release (e.g., file handling) using the `with` statement.

11. **How is memory managed in Python?**
- Python uses an automatic memory management system that includes a private heap, garbage collection, and reference counting.

12. **Generators vs Iterators**
- Generators are a simple way to create iterators using functions and the `yield` statement.
- Iterators are objects that implement the iterator protocol, consisting of the `__iter__()` and `__next__()` methods.

13. **Why is Python called a dynamically typed language?**
- Python is called a dynamically typed language because variable types are determined at runtime, allowing for more flexibility in coding.
- This means you can reassign variables to different data types without explicit type declarations.

14. **Why is Python called an interpreted language?**
- Python is called an interpreted language because its code is executed line by line by an interpreter, rather than being compiled into machine code beforehand. This allows for easier debugging and faster development cycles.

15. **What is passed by reference and passed by value?**
- In Python, mutable objects (like lists and dictionaries) are passed by reference, meaning changes made to the object within a function affect the original object.
- Immutable objects (like strings and tuples) are passed by value, meaning changes made to the object within a function do not affect the original object.

16. **What is pass?**
- The `pass` statement in Python is a null operation; it is syntactically required but you do not want any command or code to execute. It is often used as a placeholder in loops, functions, or classes.

17. **What is the Difference between List and Array in Python?**
- A list is a built-in Python data structure that can hold elements of different data types and is dynamic in size.
- An array (from the `array` module) is a more efficient data structure that can only hold elements of the same data type and is more memory efficient for large datasets.

18. **What are Python's built-in data types?**
- Python's built-in data types include:
  - Numeric Types: `int`, `float`, `complex`
  - Sequence Types: `list`, `tuple`, `range`
  - Text Type: `str`
  - Mapping Type: `dict`
  - Set Types: `set`, `frozenset`
  - Boolean Type: `bool`
  - Binary Types: `bytes`, `bytearray`, `memoryview`

19. **What are Modules and Packages in Python?**
- A module is a single Python file that contains definitions and statements. It can be imported and used in other Python programs.
- A package is a collection of related modules organized in a directory hierarchy.


20. **Sort and Sorted in Python**
- `sort()` is a method that modifies a list in place to arrange its elements in a specific order (ascending by default).
- `sorted()` is a built-in function that returns a new sorted list from the elements of any iterable, leaving the original iterable unchanged.  

21. Join vs Merge in Python
- `join()` is a string method used to concatenate elements of an iterable (like a list) into a single string, with a specified separator.
- `merge()` is not a built-in Python function, but it is commonly associated with the `pandas` library, where it is used to combine DataFrames based on a key.

22. **Split vs Partition vs Strip in Python**
- `split()` is a string method that divides a string into a list of substrings based on a specified delimiter.
- `partition()` is a string method that splits a string into three parts: the part before the separator, the separator itself, and the part after the separator.
- `strip()` is a string method that removes leading and trailing whitespace (or other specified characters) from a string.


23. **What is the GIL (Global Interpreter Lock) in Python?**
- The GIL is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at once. This means that in a multi-threaded Python program, only one thread can execute Python code at a time, which can be a limitation for CPU-bound tasks.

24. **Zip in Python**
- `zip()` is a built-in function that takes multiple iterables (like lists or tuples) and aggregates them into a single iterable of tuples, where each tuple contains one element from each of the input iterables.

25. Magic Methods in Python
- Magic methods (also known as dunder methods) are special methods in Python that start and end with double underscores (e.g., `__init__`, `__str__`, `__add__`). They allow you to define the behavior of your objects for built-in operations, such as initialization, string representation, and arithmetic operations.
