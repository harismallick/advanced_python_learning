# source: https://www.youtube.com/watch?v=mclfteWlT2Q&list=PLzMcBGfZo4-kwmIcMDdXSuy_wSqtU-xDP

# 1. How is Python code executed on a computer
# High level code -> translated to byte code -> byte code is interpreted by the 
# Python interpreter in real time.

# 2. Python allows you to call a function without having declared it in a class:

class Dog:
    def __init__(self):
        self.bark()

# Python file is executed normally, even though bark() is not defined.

# 3. You can declare a Class inside a function and return it to instantiate an instance of the class later.

def make_class(x: any):
    class Person:
        def __init__(self, name: str):
            self.name = name

        @property
        def get_name(self) -> str:
            return self.name
        
        def print_func_param(self) -> str:
            return print(f"Make class was instantiated with {x}")

    return Person

cls = make_class("hello world")
instance: make_class.Person = cls("John")
print(instance.get_name)
print(instance.print_func_param())

# Don't know why you'd ever do this, but it highlights how Python interprets code line-by-line
# In languages like Java or C++, you would not be able to do this.

# 4. The inspect library

import inspect

print(inspect.getsource(instance.print_func_param))
# This will print the actual lines of code for this function in the terminal.
# Can be useful for quick debugging or lookup.
# However with modern IDEs, not so necessary.

