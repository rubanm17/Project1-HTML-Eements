file = open("sample1.txt", "r")
print(file.read())
file.close()

# Read first 10 characters in the file
file = open("sample1.txt","r")
print("\nRead in parts: \n")
print(file.read(10))
file.close()

# Read first line in the file
file = open("sample1.txt", "r")
print("\nReading the first line \n")
print(file.readline())
file.close()

# Read first four lines in the file
file = open("sample1.txt", "r")
print("\nReading multiple lines \n")
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

# Looping throuh the lines in the file
file = open("sample1.txt", "r")
print("\n Looping through the lines \n")
for line in file :
    print(line)
file.close()        