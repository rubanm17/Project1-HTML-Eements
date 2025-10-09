num = int(input("Enter the number to be checked : "))

flag = False

if num > 1:
    # check for factors
    for i in range(2,num):
        flag = True
        break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")