"""
Decorator is a function that takes a function and returns a new function.
It is used to add some functionality to the existing function.
"""


def decorator(**decorator_kwargs):
    """
    This is a decorator function that takes a function and returns a new function.
    """
    all_positive = decorator_kwargs.get("all_positive", False)

    def outer_wrap(func):
        """
        This is an outer wrapper function that takes a function and returns a new function.
        """

        def wrapper(*args, **kwargs):
            """
            This is a wrapper function that takes a function and returns a new function.
            """
            first_value, second_value = args[0], args[1]
            if all_positive:
                if first_value < 0 or second_value < 0:
                    return "Please provide the positive values"
            result = func(*args, **kwargs)
            return result

        return wrapper

    return outer_wrap


@decorator(all_positive=True)
def add(a, b):
    """
    This is a function that takes two arguments and returns the sum of the two arguments.
    """
    return a + b


addition = add(1, 2)
print(addition)
