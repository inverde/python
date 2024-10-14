# Ask the user for x and y values
# Shows the nesting of functions
x = float(input("Por favor, digite el valor de x:"))
y = float(input("Por favor, digite el valor de y:"))

# Sum x + y
# Round the result to nearest integer
z = round(x + y)

print(z)

if z == 9:
    print('Calculator is right')
else:
    print(f"Calculator is giving an erronous result: {z}")
