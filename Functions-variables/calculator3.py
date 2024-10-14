# Ask the user for x and y values
x = input("Por favor, digite el valor de x:")
y = input("Por favor, digite el valor de y:")

# Sum x + y
# Without nesting of functions, convert the string to integers
z = int(x) + int(y)

print(z)

if z == int(x) + int(y):
    print('Calculator is right')
else:
    print(f"Calculator is giving an erronous result: {z}")
