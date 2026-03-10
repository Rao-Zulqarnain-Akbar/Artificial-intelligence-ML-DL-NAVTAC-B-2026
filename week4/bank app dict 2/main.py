import bankcore
import accounts


def main():
    
    print("Welcome to ABC Bank")
    
    while True:
        
        print("\n1. Create Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            
            name = input("Enter name: ")
            password = input("Enter password: ")
            
            customer_id = bankcore.create_account(name, password)
            
            accounts.balance_record[customer_id] = 0
        
        
        elif choice == "2":
            
            cid = input("Enter Customer ID: ")
            password = input("Enter password: ")
            
            if bankcore.login(cid, password):
                
                while True:
                    
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")
                    
                    option = input("Select option: ")
                    
                    if option == "1":
                        
                        amount = int(input("Enter amount: "))
                        accounts.deposit(cid, amount)
                    
                    
                    elif option == "2":
                        
                        amount = int(input("Enter amount: "))
                        accounts.withdraw(cid, amount)
                    
                    
                    elif option == "3":
                        
                        accounts.check_balance(cid)
                    
                    
                    elif option == "4":
                        
                        print("Logged out")
                        break
        
        elif choice == "3":
            
            print("Thank you for using ABC Bank")
            break
        
        else:
            print("Invalid option")


main()