a = int(input("Enter the number : "))
sum = 0
temp = a
n = len(str(temp))
while temp > 0 :
    b = temp % 10
    sum += b**n
    temp = temp // 10
if a == sum :
    print(f"{a} is an armstrong number")
else :
    print(f"{a} is not an armstrong number")               