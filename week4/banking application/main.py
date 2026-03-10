import bankcore
import accounts

def main():
    print("Welcome to ABC Bank")

    while True:

        print("\nMain Menu")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            name = input("Enter name: ")
            password = input("Enter password: ")

            customer_id = bankcore.create_account(name, password)

            accounts.balance_record.append([customer_id, 0])

            print("Account created")
            print("Your Customer ID:", customer_id)

        elif choice == "2":

            customer_id = input("Enter Customer ID: ")
            password = input("Enter Password: ")

            if bankcore.login(customer_id, password):

                while True:

                    print("\nBank Menu")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Logout")

                    option = input("Choose option: ")

                    if option == "1":

                        balance = accounts.check_balance(customer_id)
                        print("Your Balance:", balance)

                    elif option == "2":

                        amount = int(input("Enter amount: "))
                        accounts.deposit(customer_id, amount)

                    elif option == "3":

                        amount = int(input("Enter amount: "))
                        accounts.withdraw(customer_id, amount)

                    elif option =="4":
                        print("Logout")
                    else:
                        print ("Invalid option")
                        

        elif choice == "3":
            print("Thank you for using ABC Bank")
            break


main()