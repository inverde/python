# Sometimes we need to send a message several times
"""Lets write a litle program for the cat
"""
print("meaow")
print("meaow")
print("meaow")

# Define a function to print any message n times instead of three
"""Our function repeat msg need to use the structure of a loop
"""
def repeat(msg, times):
    # Test with1
    # while loop
    n = times
    while n:
        print(msg)
        n-= 1

