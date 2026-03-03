import arithmetic
import bmi
import temprature
import length

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

while True:
    print("\n===== SMART CALCULATOR =====")
    print("1. Arithmetic Operations")
    print("2. BMI Calculator")
    print("3. Temperature Converter")
    print("4. Length Converter")
    print("5. Exit")

    choice = input("Choose an option: ")

    # Arithmetic
    if choice == "1":
        a = (int("Enter first number: "))
        b = (int("Enter second number: "))

        print("1. Add \n2.Subtract \n3.Multiply \n4.Divide")
        op = input("Choose operation: ")

        if op == "1":
            print("Result:", arithmetic.add(a, b))
        elif op == "2":
            print("Result:", arithmetic.subtract(a, b))
        elif op == "3":
            print("Result:", arithmetic.multiply(a, b))
        elif op == "4":
            print("Result:", arithmetic.divide(a, b))
        else:
            print("Invalid operation!")

    # BMI
    elif choice == "2":
        weight = (int("Enter weight (kg): "))
        height = (float("Enter height (meters): "))

        bmi_value = bmi.calculate_bmi(weight, height)
        category = bmi.bmi_category(bmi_value)

        if bmi_value:
            print("Your BMI:", round(bmi_value, 2))
        print("Category:", category)

    # Temperature
    elif choice == "3":
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        temp_choice = input("Choose option: ")

        if temp_choice == "1":
            c = get_number("Enter Celsius: ")
            print("Result:", temprature.c_to_f(c))
        elif temp_choice == "2":
            f = get_number("Enter Fahrenheit: ")
            print("Result:", temprature.f_to_c(f))
        else:
            print("Invalid choice!")

    # Length
    elif choice == "4":
        print("1. Meters to KM")
        print("2. KM to Meters")
        print("3. Meters to Feet")
        print("4. Feet to Meters")

        len_choice = input("Choose option: ")

        value = get_number("Enter value: ")

        if len_choice == "1":
            print("Result:", length.meters_to_km(value))
        elif len_choice == "2":
            print("Result:", length.km_to_meters(value))
        elif len_choice == "3":
            print("Result:", length.meters_to_feet(value))
        elif len_choice == "4":
            print("Result:", length.feet_to_meters(value))
        else:
            print("Invalid choice!")

    # Exit
    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid menu choice! Try again.")