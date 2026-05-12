def prob_a_or_b(a,b,all_p_outcom):
    p_a = len(a)/len(all_p_outcom)
    p_b = len(b)/len(all_p_outcom)
    inte = a.intersection(b)
    prob_inte = len(inte)/len(all_p_outcom)
    return (p_a+p_b-prob_inte)

evens = {2,4,6}
greater_than_two = {3,4,5,6}
all_possible_outcomes = {1,2,3,4,5,6}

print("The probability of getting an even num or a num greater than 2 is:")
print(prob_a_or_b(evens,greater_than_two,all_possible_outcomes))