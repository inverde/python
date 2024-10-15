# In programming recursion is called when a program call itself
"""
Recursions are used instead of loops to iterate over multiple instructions several times
Recursions are usually more inefficient and slower than regular loops but logically
make our program very easy to understand and save the programmers numerous instructions.
"""
# Defines a recursive function to count n times

def countdown(n):
    count = n
    if not count: # Pythonic code
        return 0
    else:
        print(n)
        return countdown(n-1)

countdown(5)

counter = 0
def sum(n):
    global counter
    count = n
    if not count:
        return counter
=   else:
        counter = counter + n
        return sum(n-1)
