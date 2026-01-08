def power4(number):
    if number <= 0:
        return False
    while number % 4 == 0:
        number = number // 4
    return number == 1

n = int(input("Enter the number to find:"))
if power4(n):
    print("\nThe number is a power of 4.")
else:
    print("\nThe number is not a power of 4.")

