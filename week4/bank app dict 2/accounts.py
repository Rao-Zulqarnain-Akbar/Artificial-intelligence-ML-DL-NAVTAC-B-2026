balance_record = {}

def check_balance(customer_id):
    
    if customer_id in balance_record:
        print("Your balance is:", balance_record[customer_id])

def deposit(customer_id, amount):
    
    if customer_id in balance_record:
        balance_record[customer_id] += amount        
    print("Deposit successful")


def withdraw(customer_id, amount):
    
    if customer_id in balance_record:
        
        if balance_record[customer_id] >= amount:
            balance_record[customer_id] -= amount
            print("Withdrawal successful")
            
        else:
            print("Insufficient balance")