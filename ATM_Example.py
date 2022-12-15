print("""
*****************
Welcome to the S Bank

Transactions;

1. Check Your Balance

2. Deposit Money

3. Withdraw Money

Please write the number of the transactions.

If you want to quit the system, please write q.

"""
)

bbalance = 1000

while True:
    transaction_ = input("Please write of the transaction number:")
    if (transaction_ == "q"):
        print("Thank you. See you soon.")
        break
    elif (transaction_ == "1" ):
        print("Your balance is {} .".format(bbalance))

    elif (transaction_ == "2"):

        amount_= int(input("Please enter the amount you want to deposit:"))
        bbalance += amount_
    elif (transaction_ == "3"):
        amount_ = int(input("Please enter the amount you want to withdraw:"))
        if bbalance - amount_ < 0:
            print("Insufficient balance, please try again")
            continue
        bbalance -= amount_
    else:
        print ("Invalid Transaction code")