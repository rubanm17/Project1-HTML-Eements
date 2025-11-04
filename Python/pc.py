class person( object ):
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
        
#child class
class employee( person ):
    def __init__(self, name, idnumber,salary,post):
        self.salary = salary
        self.post = post
        #invoking the parent class properties
        person.__init__(self,name,idnumber)
#creation of an object variable on an instance
a = employee("Joy",911,789,"wps")
#calling a function of the class person using its instance
a.display()