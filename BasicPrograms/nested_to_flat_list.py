"""
This is a file that contains the code for the nested to flat list.
"""


def nested_to_flat_list(nested_list):
    """
    This is a function that takes a nested list and returns a flat list.
    """
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(nested_to_flat_list(item))
        else:
            flat_list.append(item)
    return flat_list


print(nested_to_flat_list([1, [2, 3, [4, 5]], [6, [7, [8, 9]]], 10]))
