def setOrNot(number,n):
    if number & (1<< (n-1)):
        print("SET")
    else:
        print("NOT SET")

number = int(input("enter the number:"))
n = int(input("Enter the SET bit position:"))
setOrNot(number,n)