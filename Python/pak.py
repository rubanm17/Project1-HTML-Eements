firstfile = input("Enter your first file")
secondfile = input("Enter your second file")

f1 = open(firstfile,'r')
f2 = open(secondfile,'r')

print("Contents of the first file before appending --\n",f1.read())
print("Contents of the second file before appending --\n",f2.read())

f1.close()
f2.close()

f1 = open(firstfile,'a+')
f2 = open(secondfile,'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print("Contents of the first file after appending --\n",f1.read())
print("Contents of the second file after appending --\n",f2.read())

f1.close()
f2.close()