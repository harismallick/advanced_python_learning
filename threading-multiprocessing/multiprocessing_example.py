import functools
import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor, as_completed, Future
from typing import Callable, Any

def time_function_execution[T](func: Callable[..., T]) -> Callable[..., T]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter()
        print(f"{func.__name__} execution took {round(t2 - t1, 2)} seconds.")
        return result
    return wrapper

# @time_function_execution
def simple_example(seconds: float) -> str:

    print(f"Going to sleep for {seconds} second(s)")
    time.sleep(seconds)
    return f"Woke up after {seconds} seconds(s)"

@time_function_execution
def multiprocessing_example(seconds: float) -> str:
    tasks: list[multiprocessing.Process] = []
    for _ in range(5):
        p = multiprocessing.Process(target=simple_example, args=[seconds])
        p.start()
        tasks.append(p)

    for task in tasks:
        task.join()
        print(f"Process {task.pid} complete.")

    return "Multiprocessing complete"

@time_function_execution
def futures_multiprocessing_example() -> None:
    MAX_WORKERS = 5
    timeout: list[int] = [5,4,3,2,1]

    with ProcessPoolExecutor(MAX_WORKERS) as executor:
        result_promises: list[Future[str]] = [executor.submit(simple_example, t) for t in timeout]

        for result in as_completed(result_promises):
            print(result.result())

    # Similar to the ThreadingPoolExecutor, can use the map method to get the results
    # in the same order as the process pool execution order.

    return

def main() -> None:
    # result = simple_example(1)
    # print(result)
    result = multiprocessing_example(1.5)
    print(result)
    futures_multiprocessing_example()

if __name__ == "__main__":
    main()