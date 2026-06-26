"""
Set is a collection of comma separated elements enclosed within {}
Sets are unordered and No indexing is allowed in sets
Duplicate elements are not allowed, only unique elements are allowed
Sets are mutable
"""

set1 = {101, "Python", "hi", 5.5, False}
print(set1)

# print(set1[0]) # TypeError: 'set' object is not subscriptable

print(type(set1))

set2 = {3, 1, 3, 8, 9, 4, 3}
print(set2)

print(len(set1))
print(len(set2))

# in 
print(set1)
print(5.5 in set1)
print("hello" in set1)
print("python" not in set1)

# Can all datatypes be an element of the set?
s1 = {101, 5.4, "hi", False, None}
print(s1)

# s2 = {1, 2, [10, 20, 30]} # lists cannot be element of a set

s2 = {1, 2, (10, 20, 30)}
print(s2)

# s3 = {1, 3, {10, 20, 30}} # sets cannot be element of a set

# Mutable datatypes are NOT allowed as elements of a set
# Only immutable datatypes are allowed as elements of a set

"""
Set methods
"""

# set.add(element) -> adds a new element inside the set
print(set1)

set1.add(50)
print(set1)

# set1.add(10, 20) # TypeError: set.add() takes exactly one argument (2 given)

set1.add(5.5)
print(set1)

# set.remove(element) - deletes/removes an element from the set
set1.remove('hi')
print(set1)

# set1.remove(20) # KeyError: 20

# set.discard(element)
set1.discard(False)
print(set1)
set1.discard(20)
print(set1)

# If an element does not exist in a set, remove() gives error but discard() does not give any error

# set.pop() -> deletes any random element from the set
set1.pop()
print(set1)
set1.pop()
print(set1)

"""
Union, Intersection and Difference of sets
Union: combining the elements of multiple sets
Intersection: common eleements of multiple sets
Difference: elements present in the first set, which are NOT preent in the second set
"""

s1 = {500, 300, 555}
s2 = {555, 666, 333, 111}
s3 = {100, 200, 300, 400, 500}

# union
print(s1.union(s2))
print(s1 | s2)

print(s1.union(s2, s3))
print(s1 | s2 | s3)

# intersection
print(s1.intersection(s2))
print(s1 & s2)

print(s1.intersection(s2, s3))
print(s1 & s2 & s3)


# set() -> Empty Set

# Difference
print(s1.difference(s2)) # elements in s1, but not in s2
print(s1 - s2)

print(s2 - s1)

x = {1, 4, True, 10, 4}
print(x)

y = {4, 0, 6, False, True, 6, 1}
print(y)

# Frozen sets: Immutable sets

z = frozenset({5, 3, 1, 0})
print(z)
print(type(z))

# z.add(8) # AttributeError: 'frozenset' object has no attribute 'add'

