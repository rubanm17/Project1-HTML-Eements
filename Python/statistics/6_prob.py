import random

def pro():
    R = [1,2,3,4,5,6]
    Grim = random.choice(R)
    probability = (R.count(6)/len(R))*100
    probability = round(probability, 2)
    print("The probability of getting 6 is:", probability)

    if Grim == 6:
        print("the game can be started")
    else:
        print("Roll again.best of Luck")
pro()