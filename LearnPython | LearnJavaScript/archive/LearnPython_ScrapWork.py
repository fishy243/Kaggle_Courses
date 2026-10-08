# Converting Lists to Tuples
my_list = [10, 20, 30, 40]

# Convert the list to a tuple
my_tuple = tuple(my_list)

print(my_tuple)  # Output: (10, 20, 30, 40)
print(type(my_tuple))  # Output: <class 'tuple'>
print(my_list)


# Converting a string to a tuple
char_tuple = tuple("Yo!")
print(char_tuple)  # Output: ('Y', 'o', '!')

# Converting a range to a tuple
range_tuple = tuple(range(5))
print(range_tuple)  # Output: (0, 1, 2, 3, 4)

# Convertiing a tuple back into a list using list() constructor
my_tuple = (10, 20, 30, 40)
my_list = list(my_tuple)
print(my_list)  # Output: [10, 20, 30, 40]

print(type(my_list))  # Output: <class 'list'>

#----------------------------------------------------------

# Creating Dictionaries
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "New York"}
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Creating Dictionaries using the dict() constructor
items = [("apple", 1), ("banana", 2)]
fruit_counts = dict(items) # Output: {'apple': 1, 'banana': 2}
print(fruit_counts)

# Using keyword arguments:
person = dict(name="Bob", age=25) # Output: {'name': 'Bob', 'age': 25}
print(person)

#----------------------------------------------------------

# Iterating Tuples
my_tuple = ("apple", "banana", "cherry")

# Iterate directly over the elements
for fruit in my_tuple:
    print(fruit)
# Output:
# apple
# banana
# cherry

# Example 2 - Using Index
my_tuple = (10, 20, 30)

# Iterate using index and range()
for i in range(len(my_tuple)):
    print(f"Element at index {i}: {my_tuple[i]}")
# Output:
# Element at index 0: 10
# Element at index 1: 20   
# Element at index 2: 30

# Example 3 - Using enumerate()
my_tuple = ("red", "green", "blue")

# Iterate using enumerate() to get index and value
for index, color in enumerate(my_tuple):
    print(f"Color at index {index}: {color}")
# Output:
# Color at index 0: red
# Color at index 1: green
# Color at index 2: blue

#----------------------------------------------------------

# Named Tuples
from collections import namedtuple

# Define a named tuple type
# The first argument is the name of the new named tuple type
# The second argument is a string of field names separated by spaces or a list of strings
Point = namedtuple('Point', ['x', 'y'])

# Create an instance of the named tuple
p1 = Point(x=1, y=2)
p2 = Point(3, 4) # You can also use positional arguments

print(p1.x)
# Rest @ --> learnpython_scrap_work.ipynb

#----------------------------------------------------------

my_dict = {"a": 1, "b": 2, "c": 3}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['a', 'b', 'c'])

values = my_dict.values()
print(values)  # Output: dict_values([1, 2, 3])

items = my_dict.items()
print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])

my_dict = {"a": 1, "b": 2}
keys_view = my_dict.keys()
print(keys_view)  # Output: dict_keys(['a', 'b'])

my_dict["c"] = 3
print(keys_view)  # Output: dict_keys(['a', 'b', 'c'])

person = {"name": "Alice", "age": 30}

print("Iterating keys:")
for key in person.keys():
    print(key) 

print("Iterating values:")
for value in person.values():
    print(value)

print("Iterating items:")
for key, value in person.items(): # Tuple unpacking in the loop
    print(f"{key}: {value}")

print("Iterating keys (default):")
for key in person: # Iterating a dict directly iterates its keys
    print(key)
    
#----------------------------------------------------------

# Set Operations
"""Set Operations (with Operators): Python sets support mathematical set operations using special
operators, which are often more concise than the corresponding methods."""

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union (|): Combines all unique elements from both sets. Equivalent to set1.union(set2).
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection (&): Returns elements common to both sets. Equivalent to set1.intersection(set2).
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}

# Difference (-): Returns elements in set1 that are not in set2. Equivalent to set1.difference(set2).
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}

difference_set_reversed = set2 - set1
print(difference_set_reversed)  # Output: {4, 5}

# Symmetric Difference (^): Returns elements in either set1 or set2 but not in both. 
# Equivalent to set1.symmetric_difference(set2).
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Subset (<=) and Proper Subset (<): 
# set1 <= set2 checks if set1 is a subset of set2 (all elements of set1 are in set2). 
# set1 < set2 checks for a proper subset (subset but not equal).
set_a = {1, 2}
set_b = {1, 2, 3}
print(set_a <= set_b)  # Output: True (set_a is a subset of set_b)
print(set_a < set_b)   # Output: True (set_a is a proper subset of set_b)
print(set_b < set_a)   # Output: False (set_b is not a proper subset of set_a)

# Superset (>=) and Proper Superset (>):
# set1 >= set2 checks if set1 is a superset of set2 (all elements of set2 are in set1).
# set1 > set2 checks for a proper superset (superset but not equal).
set_a = {1, 2, 3}
set_b = {1, 2}
print(set_a >= set_b)  # Output: True (set_a is a superset of set_b)
print(set_a > set_b)   # Output: True (set_a is a proper superset of set_b)

# These operators provide a clear and efficient way to perform common set operations.