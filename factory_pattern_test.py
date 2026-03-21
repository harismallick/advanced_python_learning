from abc import ABC, abstractmethod
import math

class ShapeFactory():
    @staticmethod
    def create_shape(length_of_side: int, num_side: int) -> Shape:
        if num_side == 1:
            return Circle(length_of_side)
        elif num_side == 3:
            return Triangle(length_of_side)
        elif num_side == 4:
            return Square(length_of_side)
        else:
            raise Exception("Incorrect number of sides given")
        

class Shape(ABC):  # Like 'interface Shape' in Java
    @abstractmethod
    def get_area(self):
        pass
    
    @abstractmethod
    def get_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, length_of_side: int):
        super().__init__()
        self.perimeter = length_of_side
        self.radius = None
        self.area = None
    
    def calculate_radius(self):
        self.radius = self.perimeter * 7 / 2 * 22
    
    def calculate_area(self):
        self.area = self.radius * ((22 / 7) ** 2)
    
    def get_area(self):
        self.calculate_radius()
        self.calculate_area()
        return self.area
    
    def get_perimeter(self):
        return self.perimeter

    def get_radius(self):
        self.calculate_radius()
        return self.radius
    
class Square(Shape):
    def __init__(self, length_of_side: int):
        super().__init__()
        self.length_of_side = length_of_side

    def get_area(self):
        return self.length_of_side ** 2

    def get_perimeter(self):
        return 4 * self.length_of_side

class Triangle(Shape):
    def __init__(self, length_of_side: int):
        super().__init__()
        self.length_of_side = length_of_side

    def get_area(self):
        return (math.sqrt(3) / 4) * (self.length_of_side ** 2)
    
    def get_perimeter(self):
        return 3 * self.length_of_side

# This would fail: "TypeError: Can't instantiate abstract class Square with abstract method draw"
# class Square(Shape):
#     pass

# test_circle = Circle(25)
# print(test_circle.get_area())
# print(test_circle.radius)

# test_square = Square(4)
# print(test_square.get_area())
# print(test_square.get_perimeter())

# test_triangle = Triangle(3)
# print(test_triangle.get_area())
# print(test_triangle.get_perimeter())

test_shape = ShapeFactory.create_shape(25, 1)
print(test_shape.get_area())
print(test_shape.get_radius()) # This would not work in Java because its not part of the intface definition
test_shape = ShapeFactory.create_shape(10, 3)
print(test_shape.get_area())
# print(test_shape.get_radius()) # This would not work in Java because its not part of the intface definition
test_shape = ShapeFactory.create_shape(8, 4)
print(test_shape.get_area())
