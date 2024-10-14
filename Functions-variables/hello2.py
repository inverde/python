# Demonstrate the calling of a function to say hello
# Defining a function without any parameter
# Abstraction of the user greeting using the hello function with a name argument.
# Also pays attention that hello is invoke before is defined in the program.
# Also see how the program implements the function composition of functional programming
def main():
    print(hello("Manuel Oscar"))

# Implementing the function with a return value or out parameter
# The return value is created with a formatted string function that implements substitution variables
def hello(name):
    return f"Hello, {name}!!!!!"

# Demonstrate that function must be called  before is run 
# Comment out this insturction to see the output
# main()

# print(hello("Julio Cesar"))
# print(hello("Jose Anibal"))

