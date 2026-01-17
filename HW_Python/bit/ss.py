s = input("Enter string : ")

n = len(s)
for end in range(n):
    for start in range(end + 1):
        print(s[start:end + 1])
