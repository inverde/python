# Demonstrate how to call a main function
# Demonstrate how to call function when file is only main
# Shows how to test for empty string to substitute for none or null
def main():
    name = input("Por favor, digite el nombre del saludado:? ")
    if not name:
        hello()
    else:
        hello(name)

#Define the hello function
def hello(to="World"):
    print("Hello,", to)

if __name__ == "__main__":
    main()
