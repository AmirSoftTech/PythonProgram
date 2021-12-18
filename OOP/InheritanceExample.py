class Shape:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

class Ractangle(Shape):
    def Area(self):
        ract = self.height * self.weight
        print("Area of ractangle is: ", ract)

class Triangle(Shape):
    def Area(self):
        tri = .5 * self.height * self.weight
        print("Area of triangle is: ", tri)

r1 = Ractangle(10, 10)
r1.Area()

t1 = Triangle(20, 20)
t1.Area()


