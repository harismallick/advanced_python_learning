from collections.abc import Callable
from typing import Any
import time

def decorator_func(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        print("Wrapper: executed before function call in wrapper")
        rv: any = func(*args, **kwargs)
        print("Wrapper: executed after the function call in the wrapper")
        return rv
    
    return wrapper

@decorator_func
def test_func(word: str) -> str:
    print("Operation inside the function being decorated")
    return f"This is the passed in word: {word}"

test_func_return: str = test_func("hello")
print(test_func_return)

# The *args and **kwargs is essential for making a dynamic wrapper/decorator that
# can be used to wrap functions having a wide variety of arguments.


def timer_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs) -> Any:
        start: float = time.time()
        rv: any = func(*args, **kwargs)
        end: float = time.time()
        total_time = end - start
        print(f"This function took {total_time:.3f} seconds")
        return rv
    
    return wrapper

@timer_decorator
def iterate():
    for i in range(10000000):
        pass

iterate()