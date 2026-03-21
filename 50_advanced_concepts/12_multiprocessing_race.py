# Using shared resources between threads and multiprocessing creates race conditions
# where both are updating the shared resource at the same time.
# Unexpected behaviour is avoided by using mutex, ie, locks

import multiprocessing

# def increment(n):
#     for _ in range(100_000):
#         n.value += 1

# if __name__ == '__main__':
#     number = multiprocessing.Value('i', 0)
#     p1 = multiprocessing.Process(target=increment, args=(number,))
#     p2 = multiprocessing.Process(target=increment, args=(number,))
    
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
    
#     print(number.value)  
    # Expected outcome is for this value to be 200_000
    # But the result is a smaller number: 115_452

# Now lets implement a lock:

# def increment(n, lock):
#     for _ in range(100000):
#         with lock:
#             n.value += 1

# if __name__ == '__main__':
#     number = multiprocessing.Value('i', 0)
    
#     lock = multiprocessing.Lock()
    
#     p1 = multiprocessing.Process(target=increment, args=(number, lock))
#     p2 = multiprocessing.Process(target=increment, args=(number, lock))
    
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
    
#     print(number.value)  
    # Now we get 200_000
    # Each process increments n exactly 100_000 times when the process has the lock

    # Lock creates an arbitrary lock
    # get_lock() returns the actual internal lock of multiprocessing.Value or multiprocessing.Array objects


def increment(n):
    for _ in range(100000):
        with n.get_lock():
            n.value += 1

if __name__ == '__main__':
    number = multiprocessing.Value('i', 0)
    
    # lock = multiprocessing.Lock() # No need to create a physical lock here
    
    p1 = multiprocessing.Process(target=increment, args=(number,))
    p2 = multiprocessing.Process(target=increment, args=(number,))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    print(number.value)  
    # We get 200_000 again
