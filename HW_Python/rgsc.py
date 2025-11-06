class Rectangle :
    def __init__(self, length, breadth) :
        self.length = length
        self.breadth = breadth

    def area(self) :
        a = self.length * self.breadth    
        print("Area of the Rectangle : ", a)

    def data(self) :
        print("Length : ",self.length, "and Breadth :", self.breadth) 

class Triangle :
    def __init__(self, length, breadth) :
        self.length = length
        self.breadth = breadth

    def area(self) :
        b = 0.5 * self.length * self.breadth    
        print("Area of the Triangle : ", b)

    def data(self) :
        print("Length : ",self.length, "and Breadth :", self.breadth)           

class Square :
    def __init__(self, side) :
        self.side = side

    def area(self) :
        c = self.side ** 2    
        print("Area of the Square : ", c)

    def data(self) :
        print("Side : ",self.side) 

class Circle :
    def __init__(self, radius) :
        self.radius = radius

    def area(self) :
        d=  3.14159 * self.radius ** 2   
        print("Area of the Circle : ", d)

    def data(self) :
        print("Radius : ",self.radius) 

r = Rectangle(5,10)
t = Triangle(5,10)
s = Square(4)
ci = Circle(7)

for shape in (r,t,s,ci) :
    shape.data()
    shape.area()