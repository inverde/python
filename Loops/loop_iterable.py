# Lets create a iterable to be able to loop through it
# Any object that implements iter method is a iterable
class shoppingCart:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self, start, end):
        return iterator(self, start, end)
