# [expression for item in iterable if condition]

# Create a list of squares
squares = [x**2 for x in range(10)]
print(squares)

# Filter Even Numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Lambda arguments: expression
def function_name(args):
    # Code block
    return
    
add = lambda x, y: x + y
print(add(3, 5))

# map() - Applies a function to each item in an iterable
numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)
print(list(squares))

# filter() - Filters items based on a condition
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))

# reduce() - Reduces an iterable to a single value
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)

# os module is used to interact with an os
import os

print(os.getcwd())      # Gets the current working directory
if not os.path.exists("test_dir"):
    os.mkdir("test_dir")
if os.path.exists("remove.txt"):
    os.remove("remove.txt")

# sys module provides access to system-specific parameters and functions
import sys

print(sys.argv)
print(sys.version)