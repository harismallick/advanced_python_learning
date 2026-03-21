# Source for all the code: https://github.com/GGyll/fifty-advanced-python-concepts/tree/master

# 1. Static arrays in Python

from array import array

numbers = array('i', [1,2,3])

# numbers[2] = "hello" # This wont work because array is statically typed to an array of integers

# All 'arrays' in Python are List objects that can hold any data type and supports dynamic resizing
# To restrict the type of data, use array from the array library

'''
Advantages of arrays over List objects:

1. Memory efficient
2. Type enforcement
3. Performance - Much faster to loop through arrays than List objects

Disadvantages:
- No dynamic resizing of the array
'''

# 2. Garbage collection

