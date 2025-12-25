def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Enter the smallest number: "))
b = int(input("Enter the largest number: "))

lcm = (a * b) // gcd(a, b)
print("LCM of", a, "and", b, "is", lcm)