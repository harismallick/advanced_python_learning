# Another fundamental concept of OOP where children classes inherit from parent classes
# Their attributes and methods, while adding further functionality in the child classes.
# Or modifying the existing behaviour from the parent class, ie, polymorphism

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Usage
dog = Dog("Buddy")
cat = Cat("Kitty")
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Kitty says Meow!

# This example shows how Cat and Dog didn't have constructors.
# But inherited the constructor from the parent Animal class.
# Both child classes then changed the behaviour of the speak method.

