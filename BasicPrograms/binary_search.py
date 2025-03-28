"""
This is a file that contains the code for the binary search.
"""


def binary_search(value, data):
    """
    This is a function that takes a value and a list and returns the index of the value in the list.
    """
    start, end = 0, len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == value:
            return mid, data[mid]
        elif data[mid] < value:
            start = mid + 1
        else:
            end = mid - 1
    return "Not Found"


print(binary_search(10, [0, 10, 20, 30, 40, 50]))
