# Define a float
from numpy import number


y = 1.
print(y)
print(type(y)) # Returns 1.0 <class 'float'>

# Convert float to integer with the int function
z = int(y)
print(z)
print(type(z)) # Returns 1 <class 'int'>

# Uncomment and run this code to get started!
print(int(1.2321))
print(int(1.747))
print(int(-3.94535))
print(int(-2.19774)) # Returns 1, 1, -3, -2

# Multiplying boolean by any data type
print(3 * True)
print(-3.1 * True)
print(type("abc" * False))
print(len("abc" * False)) # Returns 3, -3.1, <class 'str'>, 0

# TODO: Complete the function
beds = 1  # number of bedrooms (data type: float)
baths = 1  # number of bathrooms (data type: float)
has_basement = False  # boolean indicating if the house has a basement (data type: boolean)

def get_expected_cost(beds, baths, has_basement):
    value = 80000 + 30000 * beds + 10000 * baths + 40000 * has_basement
    value
    return value

# RETURNS: 120000

# Adding Booleans
print(False + False)
print(True + False)
print(False + True)
print(True + True)
print(False + True + True + True)

# RETURNS: 0, 1, 1, 2, 3

# Question 5: Online shop Gold plated and Solid Gold Rings
def cost_of_project(engraving, solid_gold):
    cost = 50 + 7 * engraving + 100 * solid_gold

# Corrected:
def cost_of_project(engraving, solid_gold):
    cost = solid_gold * (len(engraving) * 10 + 100) + (not solid_gold) * (len(engraving) * 7 + 50)
    return cost
