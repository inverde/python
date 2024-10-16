#Import system's modules
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), '../Conditionals')))
# Import module for conditional executions
import conditionals as condMod

# Sometimes we need to send a message several times
"""Lets write a litle program for the cat
"""
condMod.set_testing(condMod.c_OFF)

if condMod.is_testing():
    print("meaow")
    print("meaow")
    print("meaow")

def main():
    repeat("meaow", 3)

# Define a function to print any message n times instead of three
"""Our function repeat msg need to use the structure of a loop
"""
def repeat(msg, times):
    # while loop
    countdown = times
    while countdown: # Pythonic statement
        print(msg)
        countdown -=1  #Equivalent to n = n-1 decrementer

main()
