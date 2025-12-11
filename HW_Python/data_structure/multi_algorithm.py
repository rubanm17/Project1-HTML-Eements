#Loop Algorithm
def fun2(a,b) :
    multi = a * b
    return multi  

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
print(fun2(a,b))

#Nested Loop Algorithm
def fun3(a,b,n) :
    multi = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            multi = a * b
    return multi
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b :"))
n = int(input("Enter the number of iterations : "))
print(fun3(a,b,n))