# In Python, even class declarations are objects.
# They are objects of type 'type'

class Test:
    def __init__(self, name: str):
        self.name = name

t: Test = Test("John")
print(type(t))
# An instance of Test is of type Test
print(type(Test))
# But Test itself is of type Type

# Because of this, python classes can be declared like below:

Test2 = type("Test2", (), {"name": "John"})
# The () will contain any super inheritance
# {} will contain attributes to instantiate an instance of the class

t2: Test2 = Test2()
print(type(t2))
print(t2.name)

# However, this is really bad for intellisense, and classes shouldn't really be declared this way.

# Class to inherit from:
class Parent:
    def print_hi(self):
        print("Hi there")

# Method to add an attribute to the class:
def add_age_attribute(self, age: int):
    self.age = age

Test3 = type("Test3", (Parent,), {"name": "John", "add_age_attribute": add_age_attribute})

t3: Test3 = Test3()
t3.add_age_attribute(34)
print("Adding an attribute via a function to a class:")
print(t3.age)

# Now that we know how classes in Python can be defined using type()
# Lets see how the same is achieved using metaclasses

class Meta(type): # Must inherit from type
    def __new__(cls, name, bases, attrs: dict[str, any]):
        print(attrs)

        modified_attrs: dict[str, any] = {}
        for key, value in attrs.items():
            if key.startswith("__"):
                modified_attrs[key] = value
            else:
                modified_attrs[key.upper()] = value

        return type(name, bases, modified_attrs)
    
class Dog(metaclass=Meta):
    x = 8
    y = 9

    def hello(self):
        return "Hello"

# By using the metaclass, we changed the attribute names to uppercase.
# This shows how metaclasses can be used to modify class definitions

dog: Dog = Dog()
# print(dog.x) # This will not work, because the attribute is now 'X'
print(dog.X)
print(dog.HELLO())
