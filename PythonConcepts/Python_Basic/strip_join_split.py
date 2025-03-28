"""
This is a file that contains the code for the strip, join, split methods.
"""

def strip_method(string):
    """
    This is a function that takes a string and returns a string with the leading and trailing whitespace removed.
    """
    return string.strip()

def join_method(string):
    """
    This is a function that takes a list of strings and returns a string with the strings joined by a space.
    """
    return ' '.join(string)    

def split_method(string):
    """
    This is a function that takes a string and returns a list of strings.
    """
    return string.split()

string = "Hello, World!"
print(strip_method(string))
print(join_method(string))
print(split_method(string))


