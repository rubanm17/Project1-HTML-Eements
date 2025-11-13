file = open('c_r.txt','r')

file1 = open('c_rupdated.txt','w')

for line in file.readlines():

    if not (line.startswith('coding')):
            print(line)

            file1.write(line)

file.close()
file1.close()