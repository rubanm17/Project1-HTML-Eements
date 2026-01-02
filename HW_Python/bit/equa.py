# Inputs (change values 0 or 1)
A = int(input("enter the value for a:"))
B = int(input("enter the value for b:"))
C = int(input("enter the value for c:"))

top_and = A & B          
middle_or = B | C       
bottom_and = B & C      

second_and = middle_or & bottom_and

Q = top_and | second_and

print("Output Q =", Q)
