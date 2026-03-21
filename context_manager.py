# Contextg managers handle the process of entering and exiting methods/functions in Python.
# If a function throws an error, the coupled downstream functions would also error out.
# To avoid cascading disastrous outcomes, the exit process from a function should be handled gracefully
# This is done using context managers

class File:
    def __init__(self, filename: str, method: str):
        self.file = open(filename, method)

    def __enter__(self):
        print("Entered the function context")
        return self.file # Must return the file object for the 'as' clause in the context manager.

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"{exc_type}, {exc_value}, {traceback}")
        self.file.close()   # Crucial step in terms of the interpreter lock
        print("Trying to perform a graceful exit")
        if exc_type == AttributeError:
            print("Performed graceful exit")
            return True

        print("Exception not handled")
        # Returning true allows for graceful closing.
        # But true should be returned based on appropriate conditions
        # Otherwise, exception gets raised


with File("test.txt", "w") as file:
    print("Within the function decorated with context manager")
    file.write("Hello")
    raise AttributeError("Demo exception that should allows graceful closing")

with File("test.txt", "w") as file:
    print("Within the function decorated with context manager")
    file.write("Hello")
    raise FileExistsError("Demo exception that will not result in graceful closing")

