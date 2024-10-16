# Conditional execution clause
""" It is the simplest form of the simple statement
It has the same caractheristic of a funcion: a header and a body """

# Sampole conditional execution
if x > 0:
    print('x is positive')

# Abstraction passing a value, boolean expression and function
def conditional_execution(value, test, func):
    if test:
        func(value)

