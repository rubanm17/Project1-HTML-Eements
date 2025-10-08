m1 = int(input("Enter the First Subject Mark"))
m2 = int(input("Enter the Second Subject Mark"))
m3 = int(input("Enter the Third Subject Mark"))
m4 = int(input("Enter the Fourth Subject Mark"))
m5 = int(input("Enter the Fifth Subject Mark"))
subjects = int(input("Enter the Total Subjects"))

total = (m1+m2+m3+m4+m5) / subjects
print(total)

if total >= 85 :
    print("Grade is 'A'")
elif total >= 75 :
    print("Grade is 'B'")
elif total >= 65 :
    print("Grade is 'C'")
elif total >= 55 :
    print("Grade is 'D'")
elif total >= 45 :
    print("Grade is 'E'")
else :
    print("Grade is 'F'")            