"""
List and Tuple:

List: A list is a collection of items that are ordered and changeable (mutable).
Tuple: A tuple is a collection of items that are ordered and unchangeable (immutable).
"""

"""
-------------------------------------------------------------------------------
List is a collection of items that are ordered and changeable (mutable).
-------------------------------------------------------------------------------
"""
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Update list
my_list[0] = 10  # Update first element
my_list.append(6) # Add new element at the end, return None
my_list.insert(1, 5) # Insert new element at index 1, return None
my_list.remove(2) # Remove the first element with value 2 from left, return None
my_list.pop(3) # Remove element at index 3, return removed element
my_list.extend([7, 8, 9]) # Add new elements at the end (takes only iterable), return None
my_list.sort() # Sort the list, return None
my_list.reverse() # Reverse the list, return None
# my_list.clear() # Remove all elements from the list, return None


import copy
# Assign the list, creates a reference to same list object in memory.
my_list_assign = my_list

# Creates a new outer list, but inner objects (nested lists, etc.) are still references, shallow copy,
my_list_copy = copy.copy(my_list)

# Any change in one has no effect on the other., deep copy
# Recursively copies all objects (inner and outer).
my_list_deepcopy = copy.deepcopy(my_list) 

print(my_list.copy())



"""
-------------------------------------------------------------------------------
Tuple is a collection of items that are ordered and unchangeable (immutable).
-------------------------------------------------------------------------------
"""

my_tuple = (1, 2, 3, 4, 5)
# Can't update tuple
# Can't add new element
# Can't insert new element
# Can't remove element
print(my_tuple)

import copy
# Assign the tuple, creates a reference to same tuple object in memory.
my_tuple_assign = my_tuple

# Creates a new outer tuple, but inner objects (nested tuples, etc.) are still references, shallow copy,
my_tuple_copy = copy.copy(my_tuple)

# Any change in one has no effect on the other., deep copy
# Recursively copies all objects (inner and outer).
my_tuple_deepcopy = copy.deepcopy(my_tuple)

print(my_tuple)
print(my_tuple_assign)
print(my_tuple_copy)
print(my_tuple_deepcopy)

