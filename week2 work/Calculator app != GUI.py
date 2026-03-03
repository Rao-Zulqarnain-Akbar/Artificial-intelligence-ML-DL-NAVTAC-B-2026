#password checker(login)
def login():
    username = input("Enter your username: ")
    login_password = 1246

    while True:
        entered_password = int(input("Enter your password: "))
        if entered_password == login_password:
            print("Login successfully.\n")
            break
        else:
            print("Incorrect password. Try again.")

#Arithemetic operator function
def arithemetic():
    print("Perform Arithmetic Operations" )
    a = int(input("Enter first number: "))
    op = input("Enter operators")
    #print("Choose operators: +,-,*,/")
    b = int(input("Enter second number: "))
    
    if op == "+":
        print("Result" , a+b)
    elif op == "-":
        print("Result" , a-b)
    elif op == "*":
        print("Result" , a*b)
    elif op == "/":
        if b!=0:
            print("Result" , a/b)
        else:
            print("Cannot divided by zero!")
    elif op == "%":
        if a%2!= 0 or b%2 != 0:
            print("Result" , a%b)
        else:
            print("Result" , 0)
    elif op == "**":
        print("Result" , a**b)
    elif op == "//":
        print("Result" , a//b)
    else:
        print("invalid Operator!")

#Body mass indexing
def BMI_calc():
    print("Body mass Index(BMI)")
    weight = int(input("Enter weight in Kg: "))
    height_meter = int(input("Enter height in meter: "))
    height_feet = height_meter * 0.3048
    bmi = weight / (height_feet * 2)
    print("Your BMI is:", round(bmi , 2))

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")        

#Temprature converter
def temp():
    print("Temprature Converter")
    c = float(input("Enter temprature in Celcius: "))
     
    k = c + 273.15
    f = (c * 9/5) + 32
    
    print("Kelvin" , k)
    print("Farenhite" , f)
 
#Tax calculator
def tax_calculator():
    salary = int(input("Enter the salary: "))
    
    if 20000 <= salary < 30000:
        tax = salary * 0.015
        print(f"Tax on your salary is: {tax}")

    elif 30000 <= salary < 40000:
        tax = salary * 0.02
        print(f"Tax on your salary is: {tax}")

    elif 40000 <= salary < 50000:
        tax = salary * 0.025
        print(f"Tax on your salary is: {tax}")
        
    elif salary >= 50000:
        tax = salary * 0.03
        print(f"Tax on your salary is: {tax}")
        
    else:
        print(f"No tax on this amount")    
    
login()

while True:
    print("Press A for Arithmetic Operations")
    print("Press B for BMI Calculation")
    print("Press C for Temprature Converter ")
    print("Press D for Tax Calculation") 
    print("Press Q to Quit")
    
    choice = input("Enter your choice: ").upper()
    
    for i in range (1):
        match choice:
            case "A":
                arithemetic()
            case "B":
                BMI_calc()
            case "C":
                temp()
            case "D":
                tax_calculator()
            case "Q":
                print("Exiting program.....")
                break
            case "_":
                print("Invalid choice!")
         
    if choice == "Q":
        break
        
                
                    
            
                
                
                
                
                
                
    
  
    
    
    
    
    
    
    
    
    
    
    