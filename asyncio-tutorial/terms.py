# Source video for the material: https://www.youtube.com/watch?v=oAkLSJNr5zY

import asyncio

async def async_function(test_param: str) -> str:
    # Any func declaration with the async keyword is also known as a coroutine in Python
    print("This is an async coroutine function")
    await asyncio.sleep(1)
    return f"Async result: {test_param}"

async def main() -> None:

    loop = asyncio.get_running_loop()
    future = loop.create_future() # Like creating a promise in JS
    print(f"Empty future: {future}")

    future.set_result("Future result: Test")
    future_result = await future # Only futures can be awaited
    # Normal synchronous code declarations in Python cannot be awaited.

    print(future_result)
    # In Python, its uncommon to work directly with promises/futures.

    # The standard practice is to create coroutines or tasks

    # Example coroutine:
    coroutine_object = async_function("Test coroutine")
    print(coroutine_object)
    # All async function declarations return a coroutine object

    # To run the code in a coroutine, the coroutine object needs to be awaited:
    coroutine_result = await coroutine_object
    print(coroutine_result)

    # Example task:
    task = asyncio.create_task(async_function("Test coroutine task"))
    print(task)
    # All tasks are futures
    # Tasks can be queued until it is time to execute them by using the await keyword:

    task_result = await task
    print(task_result)


if __name__ == "__main__":
    # main() # This will throw an error because async functions cannot be run like normal callbacks
    asyncio.run(main()) # This creates a co-routine that can be run asynchronously by the interpreter.