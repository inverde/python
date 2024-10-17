# import sys and os module to add other directory than current to the path
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), '../Conditionals')))
import conditionals as condMod

condMod.set_testing(condMod.c_OFF)

def main():
    n = get_number()
    repeat(n, "meow")


def get_number():
    while True:
        x = int(input("Por digite el numero de iteraciones? "))
        if x < 0:
            continue
        else:
            break
    return x


def repeat(x, msg):
    for i in range(x):
        print(msg)


# Another type of loops in Python are For Loops
""" For loops loops iterate all the values of iterable sequence of values
    In Python a iterable is a class of object able to makes iterations
    There are several structures like: lists, tuples, dictionaries and collections
"""
# Lets loop through all the items of a list
if condMod.is_testing():
    for i in [0,1,2]:
        print("meow")

# We need to loop through a iterable certain number of times
# Lets use the Python iterable function range
if condMod.is_testing():
    for i in range(3):
        print("meow")

if __name__ == "__main__":
    main()

