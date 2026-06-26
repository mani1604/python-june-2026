"""
Strings: group/collection of characters enclosed within quotes
Indexing with strings
Strings are immutable
"""

s1 = "Python is a fun language."
print(s1)
print(type(s1))

print(len(s1)) # total number of characters

# Indexing
print(s1[0])
print(s1[-1])

# Concatenation
langauge = "Python"
version = "3.14.3"
print(langauge + version)

# Strings are immutable
# s1[0] = 'p' # TypeError: 'str' object does not support item assignment

# Repetition
print("Hi" * 4)

# Membership operator
s2 = "Hello World"
print('He' in s2)
print('world' in s2)

"""
Slicing of strings
------------------
Fetching a sub-string (part of the string) from the given string
string[start:end:step]
start: the starting index where we need to start slicing the string
end: ending/last index where we need to stop the slicing (end is excluded)
step: increment/decrement for performing slicing
"""
print(s2[2:6:1])
print(s2[0:4:1])
print(s2[1:8:2])
print(s2[4:9:-1]) # Empty string
print(s2[9:4:-1])
print(s2[9:3:-1])

print(s2)

print(s1[0:6:1])

# step = 1 by default
s2 = "Hello World"
print(s2[4:9:1])
print(s2[4:9:]) # by default, step = 1
print(s2[4:9])

"""
If the step is positive, by default
    - start = 0
    - end = length of the string

If the step is negative, by default,
    - start = -1 (last index)
    - end = 0 ( including 0 )
"""

print(s2[:5:1])
print(s2[3::2])
print(s2[:6:-1])
print(s2[::-2])
print(s2[::-1]) # reverse of the string

print(s2)
# print(s2[2:7:0]) # ValueError: slice step cannot be zero

"""
Methods of string
"""

# index()
print(s1)
print("index() => ")
print(s1.index("f"))
print(s1.index("n"))
# print(s1.index('z')) # ValueError: substring not found
print(s1.index("fun"))
# print(s1.index("Java")) # ValueError: substring not found
print(s1.index("age"))

# find()
print("find() => ")
print(s1.find("f"))
print(s1.find("n"))
print(s1.find('z')) # when the substring/character is not found, find() returns -1
print(s1.find("age"))
print(s1.find("Java"))

# count()
print("count() =>")
print("Occurance of 'n' is", s1.count('n'))
print("Occurance of 'a' is", s1.count('a'))
print("Occurance of 'z' is", s1.count('z'))

s3 = "Python is a fun language. We are learning Python."
print("Occurance of 'Python' is", s3.count("Python"))
print("Number of spaces are", s3.count(" "))

print(s3)
# replace() => it replaces a substring a substring with a new substring
print(s3.replace("Python", "Java")) # it gives a new string
print(s3) # the existing string is unchanged!!!

# split()
print(s1)
print(s1.split())
print(s1.split('n'))

s4 = "We are learning Python 3.14. Python is fun."
print(s4.split("Python"))

#

print(s4)

print(s4.capitalize())
print(s4.upper())
print(s4.lower())

# help(str)