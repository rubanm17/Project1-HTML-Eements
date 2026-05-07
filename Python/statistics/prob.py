import random

def prob_r():
  A=["red","blue","green"]
  res=random.choice(A)
  probability = A.count("red")/len(A)
  print("The probability of getting red is:", probability)

  if res == "red":
    print("The color red got selected.")
  else:
    print("The color red did not get selected.")

prob_r()