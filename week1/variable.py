#rules for variable
#1-not be number
#2-start with alphabets(In constant all alphabets are in great format)-->INSTITUTE="Corvit",PI=3.14
#3-meaningful,relevant
#4-no space in variable name
#5-reserved keywords are not used as variable

print("Hello")
print('haris')

#variable in working
a=5
b=3.33
c="hello"
print("the value of a is: ", a)
print("the value of b is: ", b)
print("the value of c is: ", c)

#know variable data type
print("data type of c is:", type(c))

#variable(value save into a variable called literals)
name="Zulqarnain Akbar"
age=20
country="Pakistan"
city="Mailsi"
print("My name is", name)
print("My age is", age)
print("My country name is", country)
print("My city name is", city)

#no need to variable declaration
site_name='programiz.pro'
print(site_name)

#overwritting
site_name ='apple.com'
print(site_name)

#type conversion
integer_number=123
float_number=1.23
new_number = integer_number+float_number

print("value:",new_number)
print("data type:",type(new_number))

#explict type casting
num_string = '12'
num_integer= 23
print("data type of num_string before Type casting:",type(num_string))
#after type casting
num_string = int(num_string)
print("data type of num_string after Type casting:",type(num_string))

num_sum = num_integer+num_string
print("Sum:",num_sum)
print("Data_type of num_sum:",type(num_sum))

#print statement with end parameter(It writes both lines conscuetively)
print('Good Morning!',end= '')
print('It is a rainy day')

#seprate parameter
print('New Year', 2023, 'See you soon!',sep= '. ')

#concatination(join 2 strings together inside print())
print('Programiz is ' + 'awesome.')

x = 5
y = 10
print('The value of x is {} and y is {}'.format(x,y))       

a = 5
b = 3.14
c="Hello"
print(f"Value of a is:{a},Data Type:{type(a)}")
print(f"Value of b is:{b},Data Type:{type(b)}")
print(f"Value of c is:{c},Data Type:{type(c)}")

name = input("Enter your name:")
age = input("Enter your age:")


