outputfile = open("U_f.txt",'w')
inputfile = open("reapeted.txt",'r')
lines_seen_so_far = set()
print("Elimination duplicate lines....")
for line in inputfile:
    if line not in lines_seen_so_far:
        outputfile.write(line)
        lines_seen_so_far.add(line)

inputfile.close()
outputfile.close()