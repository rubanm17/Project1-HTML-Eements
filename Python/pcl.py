class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    
    def display(self):
        print(self.firstname,self.lastname)

class Student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduateyear = year

x = Student("S","ASWIN",9999)
x.display()
print(x.graduateyear)