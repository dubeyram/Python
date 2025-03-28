"""
This is a file that contains the code for the tree constructor.
"""


def TreeConstructor(strArr):
    """
    This is a function that takes a list of strings and returns a boolean value.
    """
    parent_count = {}  # Dictionary to store parent frequencies

    for pair in strArr:
        child, parent = map(int, pair.strip("()").split(","))  # Extract numbers

        # Count parent occurrences
        parent_count[parent] = parent_count.get(parent, 0) + 1

        # If any parent has more than 2 children, return "false" early
        if parent_count[parent] > 2:
            return "false"

    return "true"


# Example usage
print(TreeConstructor(["(1,2)", "(2,4)", "(5,4)", "(6,4)"]))  # Output: "true"
print(TreeConstructor(["(1,2)", "(2,4)", "(5,4)", "(6,4)", "(7,4)"]))  # Output: "false"
