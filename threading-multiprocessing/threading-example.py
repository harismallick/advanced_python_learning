import threading
import time
from concurrent.futures import ThreadPoolExecutor, Future, as_completed

def simple_example() -> None:
    print("Going to sleep")
    time.sleep(1)
    print("Done sleeping...")
    return

def simple_example_runner() -> None:

    t1 = time.perf_counter()
    tasks: list[threading.Thread] = []

    for _ in range(5):
        task = threading.Thread(target=simple_example)
        task.start()
        tasks.append(task)

    for task in tasks:
        task.join()

    t2 = time.perf_counter()
    print(f"Running this process took {round(t2 - t1, 2)} second(s)")
    return
    
def func_w_arguments(sleep: float) -> str:
    print(f"Going to sleep for {sleep} second(s)")
    time.sleep(sleep)
    print("Done sleeping...")
    return f"Done sleeping for {sleep} second(s)"

def func_w_arguments_runner(**kwargs) -> str:
    if 'sleep' not in kwargs:
        raise AttributeError("sleep argument not found. Provide time in seconds to sleep.")
    
    t1 = time.perf_counter()
    tasks: list[threading.Thread] = []

    for _ in range(5):
        task = threading.Thread(target=func_w_arguments, args=[kwargs['sleep']])
        task.start()
        tasks.append(task)

    for task in tasks:
        task.join()

    t2 = time.perf_counter()
    print(f"Running this process took {round(t2 - t1, 2)} second(s)")

    return "Finished running the process"

def threadpool_exec_example() -> None:
    # With this method, you create a future/promise object
    MAX_WORKERS = 5
    with ThreadPoolExecutor(MAX_WORKERS) as executor:
        f1 = executor.submit(func_w_arguments_runner, sleep=2)
        print(f1.result()) # Methods being used to return a promise must have a return value

    
    timeout: list[int] = [5,4,3,2,1]

    # Example with looping through multiple tasks queued in a multithreaded list:
    # This method will return the thread result as soon as its ready
    with ThreadPoolExecutor(MAX_WORKERS) as executor:
        # Use the as_completed method to iterate through results of completed futures:
        tasks: list[Future[str]] = [executor.submit(func_w_arguments, t) for t in timeout]
        for task in as_completed(tasks):
            print(task.result())

    # Another way of doing the above is to use the map method built into ThreadPoolExecutor:
    # The map method will return the thread results IN THE SAME order as the execution
    with ThreadPoolExecutor(MAX_WORKERS) as executor:
        results = executor.map(func_w_arguments, timeout)
        for result in results:
            print(result)

    return

def main() -> None:
    # simple_example_runner()
    # func_w_arguments_runner(sleep=2)
    threadpool_exec_example()
    return

if __name__ == "__main__":
    main()