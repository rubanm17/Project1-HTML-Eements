rs = int(input("Enter the number of red shirts: "))
bs = int(input("Enter the number of blue shirts: "))
ws = int(input("Enter the number of white shirts: "))

total = rs + bs + ws

prob_a = bs/total
prob_b = rs/total

prob_b_g_a = prob_b
prob_a_b = prob_a * prob_b

print("The probability of getting a red shirt second is:")
print(round(prob_b_g_a,3))

print("The probability of getting a red shirt second is:")
print(round(prob_a_b,3))