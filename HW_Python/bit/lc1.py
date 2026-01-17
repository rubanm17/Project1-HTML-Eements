n = int(input("Enter your number: "))

binary = bin(n)[2:]   
max_count = 0
current_count = 0

for bit in binary:
    if bit == '1':
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0

print("Longest consecutive 1's length :", max_count)
