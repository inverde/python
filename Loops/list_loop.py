# import sys and os module to add other directory than current to the path
import sys, os
os.path.join(os.path.directory(__name__), '../Conditionals')
import Conditionals as condMod


# Another type of loops in Python are For Loops
""" For loops loops iterate all the values of iterable sequence of values
    In Python a iterable is a class of object able to makes iterations
    There are several structures like: lists, tuples, dictionaries and collections
"""
# Lets loop through all the items of a list
for i in [0,1,2]:
    print("meow")

# We need to loop through a iterable certain number of times
# Lets use the Python iterable function range
for i in range(3):
    print("meow")

