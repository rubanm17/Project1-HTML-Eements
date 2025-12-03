fn = open('c_r.txt','r')

fnn = open('c_ru.txt','w')

cont = fn.readlines()
type(cont)
for i in range(1, len(cont)+1):
    if(i % 2  != 0):
        fnn.write(cont[i-1])
    else:
        pass

fnn.close()

fnn = open('c_ru.txt','r')

cont1 = fnn.read()

print(cont1)
      
fn.close()
fnn.close()