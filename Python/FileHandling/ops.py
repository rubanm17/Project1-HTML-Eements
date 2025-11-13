file =  open('c_r.txt','r')
print(file.read())
file.close()
file = open('c_r.txt','r')
print("\nRead in parts\n")
print(file.read(8))
file.close()

file =  open('c_r2.txt','w')
file.write("Hi! I am Penguin and I am 1 year old.")
file.close()

