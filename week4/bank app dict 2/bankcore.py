branch_id = 2057
user_number = 1

users_info = {}


def create_account(name, password):
    
    customer_id = str(branch_id) + "-" + str(user_number)
    users_info[customer_id] = {"name": name,"password": password}
    
    user_number += 1
    
    print("Account created successfully")
    print("Your Customer ID:", customer_id)
    
    return customer_id


def login(customer_id, password):
    
    if customer_id in users_info:
        
        if users_info[customer_id]["password"] == password:
            print("Login Successful")
            return True
        
    print("Invalid login")
    return False