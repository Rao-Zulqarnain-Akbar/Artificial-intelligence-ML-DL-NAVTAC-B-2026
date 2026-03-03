import tkinter as tk
from tkinter import messagebox

# ------------------ LOGIN WINDOW ------------------ #
def check_login():
    if password_entry.get() == "1246":
        messagebox.showinfo("Success", "Login Successfully!")
        login_window.destroy()
        main_menu()
    else:
        messagebox.showerror("Error", "Incorrect Password!")

login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x200")

tk.Label(login_window, text="Username").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Password").pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

tk.Button(login_window, text="Login", command=check_login).pack(pady=10)


# ------------------ MAIN MENU ------------------ #
def main_menu():
    menu = tk.Tk()
    menu.title("Main Menu")
    menu.geometry("400x300")

    tk.Button(menu, text="Arithmetic", width=20, command=arithmetic_window).pack(pady=5)
    tk.Button(menu, text="BMI Calculator", width=20, command=bmi_window).pack(pady=5)
    tk.Button(menu, text="Temperature Converter", width=20, command=temp_window).pack(pady=5)
    tk.Button(menu, text="Tax Calculator", width=20, command=tax_window).pack(pady=5)
    tk.Button(menu, text="Quit", width=20, command=menu.destroy).pack(pady=5)

    menu.mainloop()


# ------------------ ARITHMETIC ------------------ #
def arithmetic_window():
    win = tk.Toplevel()
    win.title("Arithmetic")

    tk.Label(win, text="First Number").pack()
    a = tk.Entry(win)
    a.pack()

    tk.Label(win, text="Operator (+,-,*,/,%,**,//)").pack()
    op = tk.Entry(win)
    op.pack()

    tk.Label(win, text="Second Number").pack()
    b = tk.Entry(win)
    b.pack()

    def calculate():
        try:
            num1 = float(a.get())
            num2 = float(b.get())
            operator = op.get()

            result = eval(f"{num1}{operator}{num2}")
            messagebox.showinfo("Result", f"Result: {result}")
        except:
            messagebox.showerror("Error", "Invalid Input!")

    tk.Button(win, text="Calculate", command=calculate).pack(pady=5)


# ------------------ BMI ------------------ #
def bmi_window():
    win = tk.Toplevel()
    win.title("BMI Calculator")

    tk.Label(win, text="Weight (kg)").pack()
    weight = tk.Entry(win)
    weight.pack()

    tk.Label(win, text="Height (meters)").pack()
    height = tk.Entry(win)
    height.pack()

    def calculate_bmi():
        try:
            w = float(weight.get())
            h = float(height.get())
            bmi = w / (h ** 2)

            if bmi < 18.5:
                status = "Underweight"
            elif bmi < 25:
                status = "Normal"
            elif bmi < 30:
                status = "Overweight"
            else:
                status = "Obese"

            messagebox.showinfo("BMI Result", f"BMI: {round(bmi,2)}\nStatus: {status}")
        except:
            messagebox.showerror("Error", "Invalid Input!")

    tk.Button(win, text="Calculate BMI", command=calculate_bmi).pack(pady=5)


# ------------------ TEMPERATURE ------------------ #
def temp_window():
    win = tk.Toplevel()
    win.title("Temperature Converter")

    tk.Label(win, text="Temperature in Celsius").pack()
    celsius = tk.Entry(win)
    celsius.pack()

    def convert():
        try:
            c = float(celsius.get())
            k = c + 273.15
            f = (c * 9/5) + 32
            messagebox.showinfo("Converted",
                                f"Kelvin: {k}\nFahrenheit: {f}")
        except:
            messagebox.showerror("Error", "Invalid Input!")

    tk.Button(win, text="Convert", command=convert).pack(pady=5)


# ------------------ TAX ------------------ #
def tax_window():
    win = tk.Toplevel()
    win.title("Tax Calculator")

    tk.Label(win, text="Enter Salary").pack()
    salary_entry = tk.Entry(win)
    salary_entry.pack()

    def calculate_tax():
        try:
            salary = float(salary_entry.get())

            if 20000 <= salary < 30000:
                tax = salary * 0.015
            elif 30000 <= salary < 40000:
                tax = salary * 0.02
            elif 40000 <= salary < 50000:
                tax = salary * 0.025
            elif salary >= 50000:
                tax = salary * 0.03
            else:
                tax = 0

            messagebox.showinfo("Tax Result", f"Tax: {tax}")
        except:
            messagebox.showerror("Error", "Invalid Input!")

    tk.Button(win, text="Calculate Tax", command=calculate_tax).pack(pady=5)


login_window.mainloop()