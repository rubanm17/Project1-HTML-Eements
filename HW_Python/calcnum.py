class Calculate :
    def __init__(self, num1, num2, num3) :
        self.num1 = num1
        self.num2 = num2
        self.num3  = num3

    def add(self) :
        print("The sum of the three numbers are :", self.num1 + self.num2 + self.num3)

if __name__ == "__main__" :
    obj = Calculate(10,20,30)
    obj.add()            