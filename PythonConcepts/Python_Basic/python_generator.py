# Python Generator
"""
A generator is a function that returns an iterator. It looks like a function, but it is not. 
It is a function that returns an iterator. The iterator is an object that has a __next__() method. 
When the __next__() method is called, the generator returns the next value in the sequence. 
"""


class GeneratorUseCase:
    """
    This is a class that contains the generator functions.
    """

    def __init__(self, n) -> None:
        """
        This is the constructor of the class.
        """
        self.n = n

    def n_th_fibonacci(self):
        """
        This is a generator function that returns an iterator that generates the nth Fibonacci number.
        """

        a, b = 0, 1
        for idx in range(self.n):
            yield a
            a, b = b, a + b

    def sum_of_fibonacci(self):
        """
        This is a generator function that returns an iterator that generates the sum of the first n Fibonacci numbers.
        """
        a, b = 0, 1
        nth_sum = 0
        for idx in range(self.n):
            a, b = b, a + b
            nth_sum += a
        yield nth_sum


genrator_usecase = GeneratorUseCase(n=13)
fib = genrator_usecase.n_th_fibonacci()
print(list(fib))
