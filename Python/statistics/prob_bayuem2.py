prob_st = 0.2

prob_stpos = 0.2 * 0.8
prob_stneg = 0.02 * 0.8
prob_positive = prob_stpos + prob_stneg

prob_pos_given_st = 0.85

prob_res = (prob_st * prob_pos_given_st)/prob_positive

print("The probability is:", prob_res)
