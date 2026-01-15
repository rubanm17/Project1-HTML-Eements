def totalFips(num1,num2):
    flips = 0
    while (num1 > 0 or num2 > 0):
        t1 = (num1 & 1)
        t2 = (num2 & 1)
        if(t1 != t2):
            flips += 1
        
        num1>>=1
        num2>>=1

    return flips
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print("\nNumber of flips needed:", totalFips(num1, num2))