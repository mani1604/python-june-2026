student1 = {'roll': 101, 'name': 'John', 'percent': 81.5}

# get() - fetches the value using the key
print(student1['name'])
print(student1.get('percent'))

# print(student1["city"]) # KeyError: 'city'
print(student1.get('city'))
print(student1.get('city', 'Bangalore')) # Default value will be printed if the key is NOT present

print(student1.get("percent", 0.0))

# update() => to update the dictionary with new value or add new key value pair
print(student1)

student1.update({'percent': 83.0, 'email': 'john@etechniketan.com'})
print(student1)

student1['city'] = "Delhi"
print(student1)

# pop() => deletes the key-value pair using the key
student1.pop('name')
print(student1)

# student1.pop(101) # KeyError: 101

# help(dict)

# popitems()

student1.popitem()
print(student1)

# keys() -> returns all the keys of the dictionary as dict_keys
keys = student1.keys()
print(keys)
print(type(keys))

# values() -> returns all the values of the dictionary as dict_values
values = student1.values()
print(values)
print(type(values))

# items() -> returns the key-values pairs (tuple) as dict_items
print(student1.items())

