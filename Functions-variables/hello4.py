from hello2 import hello
""" Demonstrate printing a line with more than one print call
Shows how to import a function of another module or file.
Shows how to print without breaking to a new line
Shows use of named parameter
Shows use of escaped parameter. "\n" says Python to jump to a new line when printing.
"""

# pay attention to the used of named parameter end. Could be provided on any position without order.
# Also see the used of escaped parameter. Escaped parameter used to give special instructions to the interpreter
# print("Hello, Julio Cesar", end="\n")

print("Hello, Jose Anibal", "\n")
print("Hello, Jose Anibal", end="")

# Printing two messages in one line
#print(hello("Julio Cesar"), end="")
#print(" ", hello("Jose Anibal"))
