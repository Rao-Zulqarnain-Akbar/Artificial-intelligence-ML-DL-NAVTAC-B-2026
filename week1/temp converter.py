temp_c=int(input ('Enter the temprature in Celcius: '))

temp_k=temp_c + 273.15
print(f"Temprature in Kelvin is: {temp_k}")

temp_f=(9/5)*temp_c + 32
print(f"Temprature in Farenhite is: {temp_f}")

if(temp_c < 10):
    print("Weather is cold today")
    
elif(temp_c > 30):
    print("Weather is hot today")
    
else:
    print("It will rain today")