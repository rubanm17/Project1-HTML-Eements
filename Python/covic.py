class Parrot:

    #class attribute
    species = "bird"

    #instance attribute
    def __init__(self,name,age):
        self.name = name
        self.age=  age

#instantiate the parrot class
blu = Parrot("Blu",10)
woo = Parrot("Woo", 15)

#accessmthe class attributes
print("Blu is a {} ".format(blu.species))
print("Woo is also {} ".format(woo.species))

#access the instance attributes
print("{} is {} years old.".format(blu.name,blu.age))
print("{} is {} years old.".format(woo.name,woo.age))