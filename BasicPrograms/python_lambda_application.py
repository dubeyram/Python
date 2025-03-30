# Lambda Applications: (map, filter, reduce)

from functools import reduce

even = [i for i in range(100) if i % 2 == 0]
print(even)
print(
    list(
        map(
            str,
            [
                reduce(
                    lambda x, y: x + y,
                    list(filter(lambda a: a % 2 == 0, [i for i in range(100)])),
                )
            ],
        )
    )
)


addition = lambda *arg, a: arg[0] + arg[1] + a
print(addition(1, 2, a=13))

message = lambda **kwargs: f"Hi Team, this is lambda {kwargs.get('testing')} testing"
print(message(testing="Kwargs"))
nums = [1, 9, 3, 7, 5]
maximum_of_list = reduce(lambda x, y: x if x >= y else y, nums)
print(maximum_of_list)


def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


def exclamation(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + "!!!"

    return wrapper


@uppercase
@exclamation
def greet():
    return "hello"


print(greet())  # Output: HELLO!!!


fib_seq = lambda n: reduce(lambda x,_: x + [x[-1]+x[-2]] , range(n-2), [0,1])

print(fib_seq(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
