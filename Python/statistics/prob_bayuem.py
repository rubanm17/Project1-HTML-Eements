def find_prob(a,b):

    if a==1:
        prob_a = 0.2
        if b==1:
            prob_bga = 0.15
        elif b==2:
            prob_bga = 0.85
        else:
            print("Invalid input")
        prob_a_b = prob_a * prob_bga
        print("Probability of b given a:" , prob_bga)
        print("Probability of both the events:", prob_a_b)

    elif a==2:
        prob_a = 0.8
        if b==1:
            prob_bga = 0.25
        elif b==2:
            prob_bga = 0.75
        else:
            print("Invalid input")
        prob_a_b = prob_a * prob_bga
        print("Probability of b given a:" , prob_bga)
        print("Probability of both the events:", prob_a_b)

    else:
        print("Invalid input")

print("enter your choices:")
print("The person has strep throat: \n1. Yes \n2. No")
a = int(input("Enter your choice for a: "))

print("The person is tested positive: \n1. Yes \n2. No")
b = int(input("Enter your choice for b: "))

print("Calculating the probability:")
print(find_prob(a,b))