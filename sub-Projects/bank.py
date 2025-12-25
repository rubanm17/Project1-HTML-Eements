class bank :
    def deposit(amount, balance):
        balance = 0
        amount = int(input("Enter the amount to deposit in the account."))
        if amount > 0:
            print("amount should be greater than 0.")
        else:
            print("amount deposited successfully.")
        
        balance = balance + amount
        print(" Your current balance = ", balance)

