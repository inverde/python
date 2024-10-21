# In python we have several custom libraries at our disposal
# Lets import the random library
import random
# Generate a list random number
numbers = []
for i in range(1, 10):
    number = random.randint(1, 10)
    try:
        
    if numbers.index(number) >= 0: # Pythonic test
        numbers.append(number)
    else:
        pass

print(numbers)

