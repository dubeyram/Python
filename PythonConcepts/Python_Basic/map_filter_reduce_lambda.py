"""
    Map, Filter, Reduce is a powerful concept in Python. It allows you to perform operations on a list of items.
    Map function applies a given function to each item in a list and returns a new list with the results.
    Filter function returns a new list containing only the items that pass a given condition.
    Reduce function applies a given function to the items of a list and returns a single value.
"""

from functools import reduce


def map_function(x):
    """
    This is a function that takes an item and returns the item plus one.
    """
    return x + 1


def filter_function(x):
    """
    This is a function that takes an item and returns True if the item is greater than 5.
    """
    return x > 5


def reduce_function(x, y):
    """
    This is a function that takes two items and returns the sum of the two items.
    """
    return x + y


list_values = [1, 2, 3, 4, 5, 6]

print(
    "Result after map function: ", list(map(map_function, list_values))
)  # Output: [2, 3, 4, 5, 6, 7]

print(
    "Result after filter function: ",
    list(filter(filter_function, list_values)),
)  # Output: [6]

print(
    "Result after reduce function: ", reduce(reduce_function, list_values)
)  # Output: 21


"""
This is an example of using map, filter, and reduce together using lambda.
"""
numbers_list = [*range(1, 10)]
sum_of_square_of_even_numbers = reduce(
    lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers_list))
)
print(sum_of_square_of_even_numbers)
