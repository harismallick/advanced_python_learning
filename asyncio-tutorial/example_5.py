import asyncio
import time


async def fetch_data(param):
    print(f"Do something with {param}...")
    time.sleep(param) # time module is NOT async compatible
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    result1 = await task1
    print("Task 1 fully completed")
    result2 = await task2
    print("Task 2 fully completed")
    return [result1, result2]


t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2 - t1:.2f} seconds")

# This example shows what happens if you try to use asyncio with modules that do not support it.
# Short answer, it doesn't work.
# Even though tasks 1 and 2 are added to the event loop, the time module doesn't
# know how to suspend itself in the event loop.
# So, the time module ends up blocking the event loop, the sleep timer is complete.
# This naturally turns this code from async back to synchronous execution.
# Time of execution is back to 3 seconds.