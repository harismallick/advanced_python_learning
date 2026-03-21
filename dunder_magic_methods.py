# These methods add unique functionality to classes in Python.
# The entire list of them can be accessed here: https://docs.python.org/3/reference/datamodel.html

class Example:
    def __init__(self, name: str):
        self.__name = name

    def __repr__(self):
        return f"My name is {self.get_name}"
    
    @property
    def get_name(self):
        return self.__name
    
    def __mul__(self, multiple: int):
        if not isinstance(multiple, int):
            raise TypeError("Multiple must be of type integer.")
        
        self.__name = self.__name * multiple
        return self.get_name
    
    def __call__(self, num: int):
        return f"Calling this class with number {num}"
    

instance: Example = Example("John")
print(instance)
print(instance * 5)
print(instance(7))


    
