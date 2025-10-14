#this function adds 2 numbers
def add(x,y):
    return x + y

#this function subtracts 2 numbers
def subtract(x,y):
    return x - y

#this function multiplies 2 numbers
def multiply(x,y):
    return x * y

#this function devides 2 numbers
def Quotient(x,y):
    return x / y

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

print("Sum : ", add(num1,num2))
print("Difference : ", subtract(num1,num2))
print("Product : ", multiply(num1,num2))
print("Quotient : ", Quotient(num1,num2))