# Lets create a iterable to be able to loop through it
# Any object that implements iter method is a iterable
class shoppingCart:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = end - start

    def __iter__(self):
        return shoppingCartIterator(self.start, self.end)

    @property
    def count(self):
        return self.count

    @count.setter
    def count(self, new_count):
        if new_count >= 0:
            self.count = new_count
        else:
            raise ValueError

class shoppingCartIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __next__(self):
        if self.current <= self.end:
            current = self.current
            self.current += 1
            return current
        else:
            raise StopIteration

myShoppingCart = shoppingCart(0,5)

for i in myShoppingCart:
    print(i)
