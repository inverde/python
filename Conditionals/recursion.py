# In programming recursion is called when a program call itself
"""
Recursions are used instead of loops to iterate over multiple instructions several times
Recursions are usually more inefficient and slower than regular loops but logically
make our program very easy to understand and save the programmers numerous instructions.
"""
# Defines a recursive function to count n times
counter = 0

def countdown(n):
    count = n
    global counter
    if not count: # Pythonic code
        return 0
    else:
        counter = n + countdown(n-1)
        return countdown(n-1)

countdown(5)
print(counter)
