# The most popular implementation of python is CPython
# It is compiled to byte code and ran on the CPython virtual machine
# In Python, everything is an object, with references to these objects.
# Python interpreter keeps a counter for the references to an object.
# If the references every become 0, then the object is garbage collected.

# The GIL is the global interpreter lock.
# It ensures that only one thread can perform its operation at a time.
# This is to ensure multiple threads cannot operate on shared object resources,
# as doing so can lead to race conditions and unexpected behaviour.

# The GIL is passed from thread to thread, each taking turns performing operations.
# This is why Python can't achieve true paralellism FOR CPU BOUND TASKS: like mathematical computations, compression-decompression, crypto
# Exceptions
# IO bound tasks can be paralellised as GIL lock is released during IO operations
# Multiprocessing:
    # This is achieved by breaking a larger process into subprocesses.
    # Running each subprocess on its own Python interpreter, with its own GIL.

import threading
import time

def cpu_task():
    for _ in range(10**7):
        pass  # Simulates CPU work

threads = [threading.Thread(target=cpu_task) for _ in range(4)]

start = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()   # This line tells python to wait for the threads to finish their work
                    # before the interpreter moves onto the next line in the file!

print(f"Time taken: {time.time() - start}")
# 0.35 seconds

# Now single thread:
start = time.time()
cpu_task()
print(f"Time taken: {time.time() - start}")
# 0.07 seconds

# Diving the task across threads was slower than doing it on a single thread!
# This demonstrates that only one thread can operate at a time.
# The increased time comes from the overhead of passing the GIL around threads.
# In official terms, its called GIL contention and context switching overhead.
