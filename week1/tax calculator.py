salary = float(input("Enter your salary: "))
if 0>=5000:
    tax=salary*0.02
    print(f"tax: {tax}")
    
elif 5000>=10000:
    tax=salary*0.03
    print("tax: {tax}")
    
elif 10000>=15000:
    tax=salary*0.04
    print("tax: {tax}")
    
elif 15000>=20000:
    tax=salary*0.05
    print("tax: {tax}")
    
elif 20000>=250000:
    tax=salary*0.06
    print("tax: {tax}")
    
else:
    print("Invalid amount")
    
