balance_record = []

def check_balance(customer_id):
    for record in balance_record:
        if record[0] == customer_id:
            return record[1]

def deposit(customer_id, amount):
    for record in balance_record:
        if record[0] == customer_id:
            record[1] += amount
            print("Deposit successful")
            return

def withdraw(customer_id, amount):
    for record in balance_record:
        if record[0] == customer_id:
            if record[1] >= amount:
                record[1] -= amount
                print("Withdrawal successful")
            else:
                print("Insufficient balance")
            return