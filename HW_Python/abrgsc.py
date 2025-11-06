#import neccesary packages
from abc import ABC, abstractmethod

#create a base class
class Shapes(ABC):
    def area(self):
        pass

class Rectangle(Shapes):
    def area(self):
        print("Area of the rectangle : length * breadth")

class Triangle(Shapes):
    def area(self):
        print("Area of the Triangle : 1/2 * length * breadth")

class Square(Shapes):
    def area(self):
        print("Area of the Square : side ** 2")

class Circle(Shapes):
    def area(self):
        print("Area of the circle : 22/7 * radius ** 2")

#driver code
r = Rectangle()
r.area()

t = Triangle()
t.area()

s = Square()
s.area()

c = Circle()
c.area()