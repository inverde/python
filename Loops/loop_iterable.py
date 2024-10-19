# Lets create a iterable to be able to loop through it
# Any object that implements iter method is a iterable
class shoppingCart:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return shoppingCartIterator(self.start, self.end)

class shoppingCartIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __next__(self):
        if self.current < self.end:
            current = self.current
            self.current += 1
            return current
        else:
            raise stopIteration

myShoppingCart = shoppingCart(1,5)

for i in myShoppingCart:
    print(i)
