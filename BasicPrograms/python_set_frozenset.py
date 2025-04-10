# Set is mutable, unordered, collecition of unique elements
# FrozenSet is immutable versin of set.


set_, dict_ = {1, 2, 3}, {1: 2}

set_.add(4)

# For updating in set we can use elements in any iterable form (list, tuple, set)
set_.update((5, 6, 7))

# Use remove if sure that element exist, otherwise discard
# set_.remove(1)
set_.discard(11)

# Pop to remoe first element of set
# set_.pop()

# Clear to make the set empty
# set_.clear()

# copy to make a soft_copy of set
set_1 = set_.copy()

# Create Deepcopy
import copy

set_2 = copy.deepcopy(set_1)


print(set_, type(set_))
print(set_1, type(set_1))
print(set_2, type(set_2))

# Iterate Over the set
for i, j, k in zip(set_1, set_2, set_):
    print(i, j, k)

# Set Union
set_3 = set_.union(set_1)
print("Set3", set_3)

set_4 = set_.intersection(set_1)
set_4.update([11, 12, 13])

print("set_4", set_4)
set_5 = set_4.difference(set_)
print("set_4", set_4, set_5)

# Frozenset

frozen_set = frozenset([1, 2, 3, 4])

frozen_set = frozen_set.union(set_1)
print(frozen_set)

print(frozen_set.isdisjoint(set_))

for i in frozen_set:
    print(i)
