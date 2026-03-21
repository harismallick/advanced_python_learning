# Abstraction is the concept of hiding business logic from the consumer of the class.
# The consumer doesn't care about how the class was implemented, just on what the class does.
# ABC classes are like interfaces from Java.
# If a class that inherits from the ABC class doesn't implement it correctly, then Python will throw an error.
# Ensures consistency across class definitions.

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Abstract base class.
    Defines a strict contract for all shapes.
    """

    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        pass

# Cannot instantiate an abstract class
# shape = Shape()  # Raises TypeError

class Rectangle(Shape):
    """
    Concrete implementation of Shape.
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


shape = Rectangle(5, 10)
print(shape.area())       
print(shape.perimeter())