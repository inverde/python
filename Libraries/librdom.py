# In python we have several custom libraries at our disposal
# Lets import the random library
import random
# Generate a list random number
numbers = []
while True:
    number = random.randint(1, 10)
    if number not in numbers:
        numbers.append(number)
        if len(numbers) == 10:
            break
print(numbers)
print()
random.shuffle(numbers)
print(numbers)
random.shuffle(numbers)
print(numbers)
random.shuffle(numbers)
print(numbers)

