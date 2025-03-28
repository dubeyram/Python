"""
This is a file that contains the code for the zip function.
"""

from itertools import zip_longest


def zip_(**kwargs):
    """
    This is a function that takes a variable number of lists and returns a zip object.
    """
    lists = kwargs.values()  # Extract all lists
    return zip(*lists)


def zip_longest_(**kwargs):
    """
    This is a function that takes a variable number of lists and returns a zip object.
    """
    lists = kwargs.values()  # Extract all lists
    return zip_longest(*lists, fillvalue="None")


# Example Usage:
print(list(zip_(list1=[1, 2, 3], list2=[4, 5], list3=[6, 7, 8, 9])))
print(list(zip_longest_(list1=[1, 2, 3], list2=[4, 5], list3=[6, 7, 8, 9])))
