class student:
    grade = 12
    name = "KingFisher"

    def intro(self):
        print("hi, i am a student")

    def det(self):
        print("My name is ", self.name)
        print("I study in Grade ", self.grade)

ob = student()
ob.intro()
ob.det()