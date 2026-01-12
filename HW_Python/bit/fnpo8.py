def power8(number):
    if number <= 0:
        return False
    while number % 8 == 0:
        number = number // 8
    return number == 1

n = int(input("Enter the number to find:"))
if power8(n):
    print("\nThe number is a power of 8.")
else:
    print("\nThe number is not a power of 8.")