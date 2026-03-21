# Concurrency is handling multiple tasks at the same time but not carrying them out in parallel.

# Similar to multithreading, it works on the concept of context switching.
# The interpreter is switching between the different tasks its handling.
# Only one task is active at any given time.

# Parallelism

# Executing multiple tasks simultaneously on different processors.
# All tasks progress simultaneously.
# Similar to multiprocessing

'''
Challenges with concurrency

1. Thread safety
    - Concurrent tasks may share common resources in memory, leading to race conditions
    - Use locks, sephamores or thread-safe data structures

2. Deadlocks
    - This occurs when two tasks block eachother indefinitely, waiting for the same resource

3. Debugging complexity
    - Non-deterministic behaviour can be harder to reproduce and debug

4. GIL limitations
    - Only one concurrent task can be performed at a time.
'''