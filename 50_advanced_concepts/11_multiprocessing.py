# Multiprocessing involves executing tasks in parallel such that each task
# runs on its own CPU core with its own python interpreter and a GIL lock.

'''
Advantages

1. This is the truest form of parallelism in Python
2. Best for CPU-bound tasks to leverage multi-core usage.
3. Each process has its own independent memory space, so reduced chance of data corruption

'''

'''
Disadvantages

1. More higher overhead than spinning up multiple threads.
2. Sharing data between processes requires additional mechanisms like queues and shared memory
3. Spawning these processes takes longer, so not suitable for short-lived tasks
'''

from multiprocessing import Process
import os

def worker(name):
    print(f"Process {name} is running in process ID: {os.getpid()}")

if __name__ == "__main__":
    process1 = Process(target=worker, args=("A",))
    process2 = Process(target=worker, args=("B",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Both processes finished")