from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    @abstractmethod
    def Area(self):
        pass

class Triangle(Shape):
    def Area(self):
        result1 = 0.5 * self.v1 * self.v2
        print("Triangle:", result1)

class Rectangle(Shape):
    def Area(self):
        result2 = self.v1 * self.v2
        print("Triangle:", result2)

tr = Triangle(8,8)
tr.Area()

re = Rectangle(5,5)
re.Area()
