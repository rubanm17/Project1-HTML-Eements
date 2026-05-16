rb = 1
bb = 6
wb = 3

total = rb + bb + wb   

prob_w = wb/total

prob_a  = prob_w * prob_w

print("the probabilityn of getting hwite ball:")
print(round(prob_w,3))

print("The probability of getting a white ball as first and second is:")
print(round(prob_a,3))