'''
Think of a memoryview as a window that lets you look at and manipulate the internal
data of an object (like a bytes or bytearray object) without actually copying it.

In standard Python, if you take a "slice" of a large byte string, Python creates 
a new copy of that data. If your file is 1GB and you slice it, you suddenly need 
2GB of RAM. A memoryview avoids this by sharing the same memory buffer.

When you wrap an object in memoryview, you are creating a mapping to the original 
memory address. Any slice you take of that memoryview is just a smaller window 
looking at the same bytes.

'''

# Traditional slicing (Creates a copy)
data = bytearray(b"Hello World")
part = data[0:5]  # A new 5-byte object is created in RAM

# Memoryview slicing (Zero copy)
mv = memoryview(data)
part_mv = mv[0:5]  # No new data is created; it just points to 'Hello'
print(part_mv) # Shows memory address of the first element in the slice

'''
Common use cases

1. Extreme Performance: It is essential when handling large binary data, such as 
video frames, network packets, or massive scientific datasets.

1. In-Place Modification: If the underlying object is mutable (like a bytearray), 
you can change the data through the memoryview.

3. Type Casting: You can tell Python to look at the bytes differently. For example, 
you can take a buffer of bytes and view it as a list of integers or doubles without 
converting the data.
'''

original = bytearray(b"ABCDE")
view = memoryview(original)

# Modify a slice of the view
view[1:3] = b"ZZ"

print(original) 
# Output: bytearray(b"AZZDE")

'''
memoryview ONLY works with data types that support the Buffer Protocol.
In simple terms, only datatypes that are stored as contiguous blocks of memory.

In Python, this means the following data types:

bytes and bytearray: Raw ASCII or binary data.

array.array: A typed array (e.g., a list of only integers or only floats).

NumPy Arrays: The gold standard for memoryview usage in data science.
'''