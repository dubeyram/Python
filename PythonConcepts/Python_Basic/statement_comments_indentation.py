# Python Statement_Coments_Indentation


def python_statement():
    """
    Instructions that a Python interpreter can execute are called statements. 
    For example, a = 1 is an assignment statement. if statement, for statement, while statement, etc.
    are other kinds of statements which will be discussed later.

    Multi-line statement
    In Python, the end of a statement is marked by a newline character. But we can make a statement extend over multiple lines with the line continuation character (\). For example:

    a = 1 + 2 + 3 + \
        4 + 5 + 6 + \
        7 + 8 + 9
    This is an explicit line continuation. In Python, line continuation is implied inside parentheses ( ), brackets [ ], and braces { }. For instance, we can implement the above multi-line statement as:

    a = (1 + 2 + 3 +
        4 + 5 + 6 +
        7 + 8 + 9)
    Here, the surrounding parentheses ( ) do the line continuation implicitly. Same is the case with [ ] and { }. For example:

    colors = ['red',
            'blue',
            'green']
    We can also put multiple statements in a single line using semicolons, as follows:

    a = 1; b = 2; c = 3

    """
    pass


print(python_statement.__doc__)
