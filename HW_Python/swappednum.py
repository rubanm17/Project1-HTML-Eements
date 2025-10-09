x = int(input("Enter the Firt value : "))
y = int(input("Enter the Second value : "))
z = int(input("Enter the Third value : "))
print(f"The value of x is {x}")
print(f"The value of y is {y}")
print(f"The value of z is {z}")
temp = x
x = y
y = z
z = temp
print(f"The swapped value of x is {x}")
print(f"The swapped value of y is {y}")
print(f"The swapped value of z is {z}")