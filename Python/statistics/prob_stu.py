def a_and_b(a,b):

    if a==1:
        prob_stu = 0.3
        if b==1:
            prob_din = 0.75
        else:
            prob_din = 0.25
    print("The probability of a given b:", prob_din)

    if a==2:
        prob_stu = 0.7
        if b==2:
            prob_din = 0.6
        else:
            prob_din = 0.4
    print("The probability of a given b:", prob_din)

    prob_a_and_b = prob_stu * prob_din
    return round(prob_a_and_b, 2)

print("Check the probability of any event occuring. First enter your choices.")

print("Is the student a Freshman? \n1. Yes \n2. No")
a = int(input("Enter your choice:"))

print("Is the student eating in dining hall? \n1. Yes \n2. No")
b = int(input("Enter your choice:"))

print("Here is the probability of both the events occurring:", a_and_b(a, b))