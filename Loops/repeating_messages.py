# Add the parent directory to the system path
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), '../Conditionals')))
import conditionals as condMod
# Sometimes we need to send a message several times
"""Lets write a litle program for the cat
"""
condMod.set_testing(condMod.c_OFF)

def main():
    repeat("meaow", 3)

if condMod.is_testing():
    print("meaow")
    print("meaow")
    print("meaow")

# Define a function to print any message n times instead of three
"""Our function repeat msg need to use the structure of a loop
"""
def repeat(msg, times):
    # while loop
    n = times
    while n: # P
        print(msg)
        n -=1  #Equivalent to n = n-1

main()
