# An Iterator object is defined with two core dunder methods:
# __iter__ and __next__
# Once you reach the end of the iteration, a StopIteration exception is raised

class MyIterator:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # An iterator must return itself.

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Signal the end of iteration.
        value = self.current
        self.current += 1
        return value

# Using the iterator
iterator = MyIterator(1, 5)
for num in iterator:
    print(num)  # Output: 1, 2, 3, 4


## Generators

# These use a lazy-loading approach to provide the next element in an iterable object
# It uses the yield keyword

'''
def stream_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Usage
for clean_line in stream_large_file("massive_data.csv"):
    process(clean_line)

The yield Keyword: Unlike return, which destroys the function's local state and exits, 
yield "freezes" the function. It hands a value to the caller and waits right there.

Memory Footprint: The memory usage stays constant (O(1) space complexity relative to 
file size) because only one line exists in your active memory buffer at any given time.

The State Machine: Python keeps track of where the file pointer is. When the loop 
asks for the "next" item, the function resumes exactly where it left off.
'''

