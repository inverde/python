# In python we have several custom libraries at our disposal
# Lets import the random library
import random
# Generate a list random number
numbers = []
while True:
    number = random.randint(1, 10)
    try:
        idx = numbers.index(number)
    except ValueError:
        numbers.append(number)
        if len(numbers) == 10:
            break

print(numbers)

