"""
args and kwargs are used to pass a variable number of arguments to a function.
args is used to pass a non-keyworded, variable-length argument list.
kwargs is used to pass a keyworded, variable-length argument list.
"""


def user_data(frist_name, *args, **kwargs):
    """
    This function is used to show the user data
    """
    last_name = args[0]
    age = kwargs.get("age", 20)
    gender = kwargs.get("gender", 20)
    return f"Name: {frist_name} {last_name} Age: {age} Gender: {gender}"


print(user_data("John", "Doe", age=25, gender="Male"))
