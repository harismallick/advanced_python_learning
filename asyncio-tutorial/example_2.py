import asyncio
import time

async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    task1 = fetch_data(1)  # Could be awaited directly
    task2 = fetch_data(2)  # Could be awaited directly
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

# While we have used async await syntax in this example, the two fetch_data tasks are NOT handled concurrently
# As we learned in examples in terms.py, calling an async function returns a coroutine object.
# When await is used on this coroutine object, all further code execution is suspended
# until the coroutine execution is scheduled and is completed.
# This means that task1 is performed first, to completion, then task2 is added to the event loop
# and performed to completion.
# So, the code in this file is actually ran SYNCHRONOUSLY, even with async await being used.
# Time for code execution: 3 seconds.