# In python we have several custom libraries at our disposal
# Lets import the random library
import random
# Generate a list random number
numbers = []
for i in range(1, 10):
    number = random.randint(1, 10)
    if numbers.index(number): # Pythonic test
    numbers.append(number)
print(numbers)

numbers.index(2)
