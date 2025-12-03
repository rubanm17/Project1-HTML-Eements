new_file = open('sample_789.txt','x')
new_file.close()

import os
print("Checking if my_file exists or not...")
if os.path.exists('sample_789.txt'):
    os.remove("sample_789.txt")
else:
    print("The file does not exists")

my_file = open('sample_789.txt','w')
my_file.write("Hello! I am penguin and I am 1 year old.")
my_file.close()

os.remove('c_r.txt')

os.rmdir('sample_565')