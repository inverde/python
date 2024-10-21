# In python we have several custom libraries at our disposal
# Lets import the random library
import random
# Generate a list random number
numbers = []
for i in range(1, 10):
    number = random.randint(1, 10)
    try:
        idx = numbers.index(number)
        numbers.append(number)
    except ValueError:
        pass

print(numbers)

