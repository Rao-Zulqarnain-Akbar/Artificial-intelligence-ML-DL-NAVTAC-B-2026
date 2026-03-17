import tkinter as tk
from tkinter import messagebox

# ---------------- VEHICLE CLASSES ----------------
class Vehicle:
    def __init__(self, vehicle_id, brand, model, rental_price_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price_per_day = rental_price_per_day
        self.is_available = True

    def rent(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_vehicle(self):
        self.is_available = True

    def calculate_rental_cost(self, days):
        return self.rental_price_per_day * days


class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day, doors, fuel):
        super().__init__(vehicle_id, brand, model, rental_price_per_day)
        self.doors = doors
        self.fuel = fuel


class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price_per_day, engine, bike_type):
        super().__init__(vehicle_id, brand, model, rental_price_per_day)
        self.engine = engine
        self.bike_type = bike_type


# ---------------- CUSTOMER ----------------
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.rented_vehicle = None

    def rent_vehicle(self, vehicle):
        if self.rented_vehicle:
            return "Already rented a vehicle"
        elif vehicle.is_available:
            if vehicle.rent():
                self.rented_vehicle = vehicle
                return f"Rented {vehicle.model}"
        return "Vehicle not available"

    def return_vehicle(self):
        if self.rented_vehicle:
            name = self.rented_vehicle.model
            self.rented_vehicle.return_vehicle()
            self.rented_vehicle = None
            return f"Returned {name}"
        return "No vehicle to return"


# ---------------- SERVICE ----------------
class RentalService:
    def __init__(self):
        self.vehicles = []
        self.customers = []

    def add_vehicle(self, v):
        self.vehicles.append(v)

    def register_customer(self, c):
        self.customers.append(c)

    def get_vehicle(self, vid):
        for v in self.vehicles:
            if v.vehicle_id == vid:
                return v
        return None


# ---------------- GUI ----------------
service = RentalService()

# Vehicles
service.add_vehicle(Bike("B101", "Honda", "CG125", 1000, "150cc", "Standard"))
service.add_vehicle(Car("C102", "Toyota", "Corolla", 4000, 4, "Petrol"))
service.add_vehicle(Car("C103", "Honda", "Civic", 6000, 4, "Petrol"))

# Customer
customer = Customer("C1", "Ali")
service.register_customer(customer)

# ---------------- TKINTER WINDOW ----------------
root = tk.Tk()
root.title("Quick Ride Rental")
root.geometry("400x400")

# ---------------- FUNCTIONS ----------------
def show_vehicles():
    text.delete("1.0", tk.END)
    for v in service.vehicles:
        if v.is_available:
            text.insert(tk.END, f"{v.vehicle_id} - {v.brand} {v.model} - {v.rental_price_per_day} PKR\n")

def rent_vehicle():
    vid = entry_vehicle.get()
    days = entry_days.get()

    if not days.isdigit():
        messagebox.showerror("Error", "Enter valid days")
        return

    vehicle = service.get_vehicle(vid)

    if vehicle:
        msg = customer.rent_vehicle(vehicle)
        if "Rented" in msg:
            cost = vehicle.calculate_rental_cost(int(days))
            msg += f"\nTotal Cost: {cost} PKR"
        messagebox.showinfo("Info", msg)
    else:
        messagebox.showerror("Error", "Invalid Vehicle ID")

def return_vehicle():
    msg = customer.return_vehicle()
    messagebox.showinfo("Info", msg)

def view_vehicle():
    if customer.rented_vehicle:
        v = customer.rented_vehicle
        messagebox.showinfo("My Vehicle", f"{v.brand} {v.model}")
    else:
        messagebox.showinfo("My Vehicle", "No vehicle rented")


# ---------------- UI ELEMENTS ----------------
tk.Label(root, text="Quick Ride Rental", font=("Arial", 16)).pack(pady=10)

btn_show = tk.Button(root, text="Show Vehicles", command=show_vehicles)
btn_show.pack(pady=5)

text = tk.Text(root, height=8, width=40)
text.pack()

tk.Label(root, text="Vehicle ID").pack()
entry_vehicle = tk.Entry(root)
entry_vehicle.pack()

tk.Label(root, text="Days").pack()
entry_days = tk.Entry(root)
entry_days.pack()

btn_rent = tk.Button(root, text="Rent Vehicle", command=rent_vehicle)
btn_rent.pack(pady=5)

btn_return = tk.Button(root, text="Return Vehicle", command=return_vehicle)
btn_return.pack(pady=5)

btn_view = tk.Button(root, text="View My Vehicle", command=view_vehicle)
btn_view.pack(pady=5)

# ---------------- RUN ----------------
root.mainloop()