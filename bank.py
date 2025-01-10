

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited:  "))

    if amount < 0:
        print("The amount should not be a negative number")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter an amount to be withdrawn:  "))

    if amount > balance:
        print("Insuffcient funds")
        return 0
    elif amount < 0:
        print("The amount should be greater than 0")
        return 0
    else:
        return amount
    
def main():
    balance = 0
    is_running = True

    while is_running:
        print("💰💰💰💰💰💰💰💰")
        print("Banking Program")
        print("💲💲💲💲💲💲💲💲")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Not valid")

    print("Thank you! Have a nice day")

if __name__ == '__main__':
    main()


