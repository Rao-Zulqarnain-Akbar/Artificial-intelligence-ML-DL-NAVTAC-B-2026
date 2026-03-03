import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_feet = float(height_entry.get())
        
        # Convert feet to meters
        height_meters = height_feet * 0.3048
        
        # Correct BMI formula
        bmi = weight / (height_meters * height_meters)
        
        result_label.config(text=f"Your BMI is: {bmi:.2f}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# Create window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x250")

# Weight Label and Entry
tk.Label(window, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(window)
weight_entry.pack()

# Height Label and Entry
tk.Label(window, text="Height (feet):").pack(pady=5)
height_entry = tk.Entry(window)
height_entry.pack()

# Calculate Button
tk.Button(window, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

# Result Label
result_label = tk.Label(window, text="")
result_label.pack(pady=10)

# Run GUI
window.mainloop()
