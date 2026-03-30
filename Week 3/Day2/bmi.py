def calculate_bmi(weight, height):
    if height <= 0:
        return "Invalid height"
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")