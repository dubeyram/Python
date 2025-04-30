"""
An iterator is a object that implements __iter__ and __next__ methods.

The __iter__ method returns the iterator objects itself.

The __next__ method return the next item in the sequence, 
when there are no items left in the sequnece it raises the StopIteration Error.

"""

class Counting:
    def __init__(self, count=1):
        self.count = count

    def  __iter__(self):
        return self

    def __next__(self):
        if self.count <=15:
            current = self.count
            self.count += 1
            return current
        else:
            raise StopIteration
        

# Creating Object 
counter = Counting()

# This for loop automatically calls __iter__ method and then repeatedly calls __next__ method until it raises StopIteration.
for count in counter:
    print(count)
        