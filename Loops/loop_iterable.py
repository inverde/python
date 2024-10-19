# Lets import system's modules to add current directory to path
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__name__), '../Conditionals')))
import conditionals as condMod
# Lets create a iterable to be able to loop through it
# Any object that implements iter method is a iterable
class shoppingCart:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self._count = end - start

    def __iter__(self):
        return shoppingCartIterator(self.start, self.end)

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, new_count):
        if new_count >= 0:
            self._count = new_count
            self.end = self._count + self.start
        else:
            raise ValueError
    def __str__(self):
        return f"shoppingCart({self.start},{self.end})"

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
            raise StopIteration

myShoppingCart = shoppingCart(0,5)

for i in myShoppingCart:
    print(i)

myShoppingCart.count = 6
print()
print(myShoppingCart.count)
print()
for i in myShoppingCart:
    print(i)
print()
print(myShoppingCart)
