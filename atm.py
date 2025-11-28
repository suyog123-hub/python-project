print("Welcome to ATM machine")

balance = 50000
pin = 1234
pin_chance = 5

while pin_chance > 0:
    user = int(input("Enter your PIN code: "))
    
    if pin == user:
        print("PIN accepted. Welcome!\n")
        print("1 --> Check your bank balance")
        print("2 --> Withdraw amount")
        print("3 --> Deposit amount")
        print("4 --> Exit")

        choose = int(input("Please choose a valid option (1-4): "))

        if choose == 1:
            print("Your total amount is", balance)

        elif choose == 2:
            withdraw_amount = int(input("Enter the withdrawal amount: "))
            if withdraw_amount <= balance and withdraw_amount <= 20000:
                balance -= withdraw_amount
                print("Your remaining amount is", balance)
            else:
                print("Invalid amount, please check it again.")
                exit()

        elif choose == 3:
            deposit_amount = int(input("Enter the deposit amount: "))
            if deposit_amount <= 20000:
                balance += deposit_amount
                print("Your remaining amount is", balance)
            else:
                print("Invalid amount, please check it again.")
                exit()

        elif choose == 4:
            print("Thanks for choosing us!")
        else:
            print("Invalid option please choose the correct option.")
        break  

    else:
        pin_chance -= 1
        if pin_chance == 0:
            print("Invalid code — your system is blocked.")
        else:
            print(f"Wrong PIN, try again. Attempts left: {pin_chance}")
