import os

# Open input files
with open("sample_file.txt", "r") as data1, open("sample_file1.txt", "r") as data2:
    
    # ---------- SPLIT WORDS ----------
    print("Words in the file are...")
    with open("sample_file.txt", "r") as f:
        for line in f:
            words = line.split()
            print(words)

    # ---------- MERGE TWO FILES ----------
    print("Merging 2 files...")
    merged_data = data1.read() + "\n" + data2.read()

    with open("mg57.txt", "w") as fp:
        fp.write(merged_data)

# ---------- CHECK IF FILE EXISTS ----------
print("Checking if mg57.txt exists or not...")
if os.path.exists("mg57.txt"):
    print("mg57.txt found!")
else:
    print("The file does not exist")

# ---------- SAFE FILE REMOVAL ----------
if os.path.exists("sample1_fileupdated.txt"):
    os.remove("sample1_fileupdated.txt")

if os.path.exists("rmdir"):
    try:
        os.rmdir("rmdir")   # Only works if folder is EMPTY
    except OSError:
        print("Directory 'rmdir' is not empty. Cannot remove.")

# ---------- DELETE DUPLICATE LINES ----------
print("Eliminating duplicate lines...")

with open("sample_file1.txt", "r") as inputfile, open("sample_file.txt", "w") as outputfile:
    seen = set()
    for line in inputfile:
        if line not in seen:
            outputfile.write(line)
            seen.add(line)

