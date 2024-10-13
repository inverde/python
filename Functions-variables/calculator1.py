import pytest

# Show unintended concatenation of strings

# Ask the user for x and y values
x = input("Por favor, digite el valor de x:")
y = input("Por favor, digite el valor de y:")

# Sum x + y
z = x + y
print(z)

def test_sum(z):
    if assert(z) == 9:
        return z
    else:
        return false


