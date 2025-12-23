def binary_to_decimal(binary):
    decimal = 0
    power = 0

    while binary > 0:
        last_digit = binary % 10
        decimal += last_digit * (2 ** power)
        binary //= 10
        power += 1

    return decimal


binary_number = int(input("Enter a binary number: "))
print("Decimal value:", binary_to_decimal(binary_number))
