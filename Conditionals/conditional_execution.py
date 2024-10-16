# Conditional execution clause
""" It is the simplest form of the simple statement
It has the same caractheristic of a funcion: a header and a body """

x = 10

# Sampole conditional execution
if x > 0:
    print('x is positive')

# Abstraction passing a value, boolean expression and function
def conditional_execution(value, test, func):
    if test:
        return func(value)

# Callig function with a lambda
"""To define a lambda function we need to write lambda plus a list of arguments optionally in parentheses
followed by a semicolon and a mathematical expression or computer expression with values and operators. """

print('Conditional Execution:', conditional_execution(10, 10 < 100, lambda x: x*x)) # Phytonic function call
