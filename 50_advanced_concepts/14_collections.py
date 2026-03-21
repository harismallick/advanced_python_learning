'''
The collections module is a staple for any Python developer who has outgrown the 
basic list, dict, and tuple. It provides high-performance container data types 
that are more specialized and memory-efficient for specific tasks.

Most common data types from the collections library:

namedtuple
defaultdict
Counter
deque
OrderedDict
'''

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)

print(p.x, p.y)  # Access by name
print(p[0])      # Access by index

from collections import defaultdict

# Groups words by their starting letter
words = ['apple', 'bat', 'alpha', 'cup']
grouped = defaultdict(list)

for word in words:
    grouped[word[0]].append(word)
    
print(grouped)
# Result: {'a': ['apple', 'alpha'], 'b': ['bat'], 'c': ['cup']}

from collections import Counter

counts = Counter(['apple', 'orange', 'apple', 'pear', 'apple', 'orange'])
print(counts.most_common(1))  # [('apple', 3)]

from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)  # Extremely fast
d.pop()          # Remove from right

# deque is clearly a doubly linked list
print(d)

