import random
def main() :
    num = [10, 25, 42, 50, 78, 89, 100]
    judge = random.choice(num)

    guess = int(input("Guess the number of the Judge : "))

    if guess == judge :
        print("Congrats, You have guess the correct Answer")
    elif guess > judge :
        print("You have chosen greater than the Judge")
    else :
        print("You have chosen lower than the Judge")
    print("The Judge chosen number is : ", judge)

main()                