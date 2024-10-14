# Demonstrate calling a function to add variables

def main():
    # Ask for inputs
    x = float(input("Digite el valor de x: ?"))
    y = float(input("Digite el valor de y: ?"))

    print(round(sum(x, y),2))

def sum(x, y):
    return x + y

main()
