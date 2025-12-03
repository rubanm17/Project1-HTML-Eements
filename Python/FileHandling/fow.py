with open('c_r.txt','w') as file:
    file.write("Hi! I am penguin and I am 1 year old.")
file.close()

with open('c_r.txt','r') as file:
    data = file.readlines()
    print("Words in the file are...")
    for line in data:
        word = line.split()
        print(word)
file.close()