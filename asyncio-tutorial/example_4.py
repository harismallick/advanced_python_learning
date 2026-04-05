import asyncio
import time


async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result2 = await task2
    print("Task 2 fully completed")
    result1 = await task1
    print("Task 1 fully completed")
    return [result1, result2]


t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")

# In this example, the order of execution of awating tasks 1 and 2 is reversed.
# Task 2, with the longer sleep timer is awaited first.
# The event loop suspends task2 and moves on to task1.
# task1 will finish first, but execution for main() coroutine WILL remain suspended
# as task2 is still being awaited.
# This means that the print statement on line 16 will not be executed until task2 coroutine is complete.
# Once this happens, then all lines of code in main() will execute simultaneously
# As there is nothing left to await for task1, as finised before task2.