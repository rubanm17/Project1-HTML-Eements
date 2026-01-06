def checkIfSum(number1,number2):
    if((number1^number2)!= 0):
        print("The numbers are not Equal.")
    else:
        print("The numbers are Equal.")

number1 = int(input("Enter the First number:"))
number2 = int(input("Enter the SSecond number:"))
checkIfSum(number1,number2)