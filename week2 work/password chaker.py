username = input("Enter your username: ")
entered_password = int(input("Enter your password: "))

login_password = 1246

while login_password != entered_password:
    print("Incorrect password.")
    entered_password = int(input("Enter your password: "))

print("Login successfully.")
 
        
        
        