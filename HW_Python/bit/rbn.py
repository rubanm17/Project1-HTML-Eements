n = int(input("Enter your original number: "))
print("Binary of Original Number is : ", bin(n)[2:])
rev = 0
temp = n

while temp > 0:
    rev = (rev << 1) | (temp & 1)
    temp >>= 1

print("Reversed Number : ", rev , " Binary Number : " , bin(rev)[2:])