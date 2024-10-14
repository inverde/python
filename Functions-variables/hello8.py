# Demonstrate to create a function with a default parameter
""" If no argument is passed function assumes the value of World
otherwise takes the passed-in parameter """

def hello(to="World"):
    print("Hello,", to)


hello()
hello("Manuel Oscar")
