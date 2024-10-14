# Ask the user for x and y values
# Shows the nesting of functions
# Demostrate to save code and instructions
x = float(input("Por favor, digite el valor de x:"))
y = float(input("Por favor, digite el valor de y:"))


print(round(x+y))

if round(x+y) == 9:
    print('Calculator is right')
else:
    print(f"Calculator is giving an erronous result: {round(x+y)}")
