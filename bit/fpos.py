import math
def printPowerSet(set,SetSize):
    powerSetSize = (int) (math.pow(2, SetSize);                      
    for outer in range(0,powerSetSize):
        for inner in range(0, SetSize):
            if((outer & (1 << inner)) > 0):
                print(set[inner],end="")
        print("")
size = int(input("Enter the array size:"))
set = []
for i in range(0,size):
    n = int input("Enter the element:")
    set.append(n)
printPowerSet(set,len(set))