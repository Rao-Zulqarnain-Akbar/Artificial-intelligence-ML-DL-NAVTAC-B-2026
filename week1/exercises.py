#exercise 1
def std_data(name="zulqarnain",age=19):
    #name = input("Enter your name:")
    #age = int(input("Enter your age:"))
    print("Your name is:" ,name)
    print("Your age is:" , age)
std_data()

#Ex2
def func1(value1 = 40,value2 = 30,value3 = 10):
    print("Printing values be:",value1,value2,value3)
func1()    
  
#Ex3
def calculation(a,b):
    sum = a+b
    subtract = a-b
    return sum, subtract
result = calculation(11,12)
print(result)

#Ex4
def show_employee(name , salary = 9000):
    print("Name:", name + "Salary:",salary)
show_employee("Sam  " , 12000)
show_employee("Sami " , )

    
    






