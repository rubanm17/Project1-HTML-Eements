mark = int(input("enter the Marks"))
sub_mark = int(input("enter the total mark"))

percentage = (mark/sub_mark)*100
print(percentage)

if percentage>=85:
  print("Grade  is 'A'")
elif percentage>=75:
  print("Grade  is 'B'")
elif percentage>=65:
  print("Grade  is 'C'")
elif percentage>=55:
  print("Grade  is 'D'")
elif percentage>=40:
  print("Grade  is 'E'")
else:
        print("Grade is 'F'")