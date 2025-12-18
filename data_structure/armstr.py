number = int(input("input: "))
result = 0
temp = number
while temp != 0:
    digit = temp % 10
    result = result+digit**3
    temp = temp//10
print(result)
if number == result:
    print("The value is a armstrong  number.")
else:
    print("the value is not an armstrong number.")