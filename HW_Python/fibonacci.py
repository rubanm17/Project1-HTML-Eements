n = int(input("Enter the number of terms to calculate: "))
a = 0
b = 1
print("Fibonacci Series of ", n ," is : ")

for i in range(n) :
    print(a, end=" ")
    a, b = b, a+b