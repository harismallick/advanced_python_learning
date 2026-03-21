# Generators are a memory-efficient way of creating an iterable
# Traditionally, you'd create an array and use a for loop.
# But this causes the entire array to be loaded into memory.
# Generators serve the next iterable element without having the entire array in memory.
import sys

class SquareGenerator:
    def __init__(self, max: int):
        self.max = max
        self.current = 0

    def __next__(self):
        return self.next()
    
    def next(self):
        if self.current == self.max:
            raise StopIteration()
        
        square: int = self.current ** 2
        self.current += 1
        return square
    
# The yield keyword automatically creates a generator, so in most cases, don't need to declare a bespoke class

def generate(max: int):
    for i in range(max):
        yield i ** 2

x = [x ** 2 for x in range(10000)]
g = generate(10000)

print(sys.getsizeof(x)) # 85176 bytes
print(sys.getsizeof(g)) # 208 bytes

print(next(g))
print(next(g))
print(next(g))
print(next(g))

# Therefore, significantly more memory efficient
# Generators maintain state. Cannot go backwards.
# Once a generator yields the last element, a StopIteration event occurs.