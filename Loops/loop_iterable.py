# Lets create a iterable to be able to loop through it
# Any object that implements iter method is a iterable
class shoppingCart:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return iterator(self.start, self.end)

class iterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __next__(self):
        if self.current < self.end:
            self.current 
