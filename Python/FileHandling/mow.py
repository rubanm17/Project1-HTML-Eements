with open('c_r2.txt') as fp:
    data1 = fp.read()

with open('sample_789.txt') as fp:
    data2 = fp.read()


data1 += "\n"
data1 += data2
print("merging 2 files...")
with open('mergingfile.txt','w') as fp:
    fp.write(data1)