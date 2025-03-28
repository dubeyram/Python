"""
This is a file that contains the code for the Fibonacci series.
"""


def fib(n):
    """
    This is a function that takes a number and returns a generator of the Fibonacci series.
    """
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fib(10)))
