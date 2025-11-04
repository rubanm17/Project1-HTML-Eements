#import neccesary packages
from abc import ABC, abstractmethod
#create a base class
class Rainbowfriends(ABC):
    
    def move(self):
        pass

class Aswin(Rainbowfriends):

    def move(self):
        print("Aswin can walk")

class Siddarth(Rainbowfriends):

    def move(self):
        print("Siddarth can talk")

class Anirudh(Rainbowfriends):

    def move(self):
        print("Anirudh can sing")

class SAswin(Rainbowfriends):

    def move(self):
        print("SAswin can play")

#driver code
r = Aswin()
r.move()

s = Siddarth()
s.move()

g = Anirudh()
g.move()

d = SAswin()
d.move()