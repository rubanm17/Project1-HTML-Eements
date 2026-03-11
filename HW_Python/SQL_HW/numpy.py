import numpy as np

# 1. Create array manually
num = np.array([0,1,2,3,4,5,6,7,8,9])
print("Original Array:")
print(num)

# 2. Replace odd numbers with -1
for i in range(len(num)):
    if num[i] % 2 == 1:
        num[i] = -1

print("\nArray after replacing odd numbers:")
print(num)

# 3. Convert to 2D array with two rows
num2d = np.array([0,1,2,3,4,5,6,7,8,9]).reshape(2,5)
print("\n2D Array:")
print(num2d)

# 4. Sum of even numbers
sum_even = 0
for i in range(len(num)):
    if num[i] % 2 == 0:
        sum_even += num[i]

print("\nSum of even numbers:", sum_even)