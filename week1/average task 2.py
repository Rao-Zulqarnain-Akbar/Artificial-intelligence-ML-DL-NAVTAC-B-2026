subject1 = input("Enter your marks in subject 1: ")
subject2 = input("Enter your marks in subject 2: ")
subject3 = input("Enter your marks in subject 3: ")

#here explict type conversion occur(convert data type)
subject1 = int(subject1)
subject2 = int(subject2)
subject3 = int(subject3)

add = subject1+subject2+subject3
average=add/2
print(average)
