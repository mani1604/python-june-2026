"""
id() => function that returns the memory address of a variable / value
Memory address: Place where the value is stored
"""

x = 1000
print(x, id(x))

y = 78.5
print(y, id(y))

name = "John"
print(name, id(name))

val = True
print(val, id(val))

n = None
print(n, id(n))
