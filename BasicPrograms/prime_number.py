"""
This is a file that contains the code for the prime number.
"""

import math


def if_prime(n):
    """
    This is a function that takes a number and returns True if the number is prime and False otherwise.
    """
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_number(n):
    """
    This is a function that takes a number and prints whether it is prime or not.
    """
    if if_prime(n):
        print(n, "is a prime number")
    else:
        print(n, "is not a prime number")


if __name__ == "__main__":
    prime_number(10)
    prime_number(11)
    prime_number(12)
    prime_number(13)
