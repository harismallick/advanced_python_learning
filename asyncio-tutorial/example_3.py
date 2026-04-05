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

# Using the create_task method adds multiple coroutines to a FIFO queue.
# In this example, there are three coroutines: main(), task1, task2
# When the event loop hits the await on line 15, it suspends the main() coroutine
# Until the task1 coroutine is fully complete.
# Inside task1, the event loop hits the await sleep on line 7.
# This suspends the task1 coroutine, until the 1 second sleep timer is complete.
# Since task2 was added to the tasks queue, the event loop can execute it while waiting for the other two coroutines.
# Once task2 hits the 2 second await on line 7, the event loop moves back to task1
# After 1 second wait, task1 is completed and removed from the tasks queue
# Then the print statement on line 16 is executed in the terminal.
# Once task2 coroutine is complete, then the event loop comes back to main() and 
# executes the print statement on line 18.
# The total execution time in this case is 2 seconds, ie, both tasks were handled concurrently.