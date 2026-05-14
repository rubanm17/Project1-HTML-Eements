def a_b(orange,blue,total):
    prob_a = orange/total

    prob_b_g_o = blue/(total-1)

    prob_a_b = prob_a * prob_b_g_o

    return round(prob_a_b,3)


orange = int(input("Enter the number of orange balls: "))
blue = int(input("Enter the number of blue balls: "))
total = orange+blue

print("The probability of getting an orange first and then a blue ball is:")
print(a_b(orange,blue,total))
