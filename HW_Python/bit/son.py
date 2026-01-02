n = int(input("Enter number: "))

if n == 0:
    print("No set bit present")
else:
    position = 1
    while n & 1 == 0:
        n >>= 1
        position += 1

    print("Position of the first set bit:", position)
