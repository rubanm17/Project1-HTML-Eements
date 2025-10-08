w_days = int(input("Total number of Working Days : "))
days_abs = int(input("Total number of Days for Absent : "))

total = (days_abs / w_days) * 100
print(total)

if total >= 95 :
    print("Out Standing Eligible for the Exam")
elif total >= 85 :
    print("Excellent Eligible for the Exam")
elif total >= 75 :
    print("Good Eligible for the Exam")        
else :
    print("Sorry, You are below 75% so cant sit for the exam")    