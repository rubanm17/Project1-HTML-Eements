class shapes:
    def area(self):
        pass
    
class rectangle(shapes):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
class triangle(shapes):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return 0.5 * self.length * self.breadth
    
class square(shapes):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

r = rectangle(5,10)
print("Area of the Rectangle : ", r.area())

t = triangle(5,10)
print("Area of the Triangle : ", t.area())

s = square(4)
print("Area of the Square : ", s.area())