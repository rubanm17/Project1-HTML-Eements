import matplotlib.pyplot as plt

student_names = ["Sanjay","Rahul","Karan","Wasia","Ramesh","Ajay","Sartaj","Priya"]
students_marks = [35,50,20,45,25,40,25,40]

marks_perc = []
for x in students_marks:
    res = (x/50)*100
    marks_perc.append(res)
print(marks_perc)

def marks_line_charts():
    plt.plot(student_names,students_marks)
    plt.title("Students Marks graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students Marks")
    plt.show()

marks_line_charts()

def percent_bar_chart():
    plt.bar(student_names,marks_perc)
    plt.title("Students Percentage graph")
    plt.xlabel("Students Names")
    plt.ylabel("Students percentage")
    plt.show()

percent_bar_chart()