branch_id = 2057
user_info = []

def create_account(name,password):
    user_number = len(user_info) + 1
    customer_id = str(branch_id)+"-"+str(user_number)
    
    user = [customer_id,name,password]
    user_info.append(user)
    
    print('Account created successfully')
    print('Your customer ID:', customer_id)
    
def login(customer_id,password):
    for user in user_info:
        if user[0]==customer_id and password[2]==password:
            print("Login successful")
            return
        else:
            print("Invalid login")
            return    
    

    