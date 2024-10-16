# Alternative execution happens when conditional statements brake into two branches

# Define a function to classify number between even and odd
def alternative_execution(n, test, main, alternate):
    if test:
        return main(n)
    else:
        return alternate(n)


# Lets execute modulus function to print if it is even or odd
alternative_execution(5, 5 % 2 == 0, lambda x: f"{x} is even", lambda x: f"{x} is odd")

