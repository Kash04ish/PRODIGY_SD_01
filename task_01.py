import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f + 459.67) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k * 9/5) - 459.67

def convert_temperature():
    try:
        temp_value = float(entry_value.get())
        unit = combo_unit.get()

        if unit == 'Celsius':
            f = celsius_to_fahrenheit(temp_value)
            k = celsius_to_kelvin(temp_value)
            result.set(f"Fahrenheit: {f:.5f}\nKelvin: {k:.5f}")
        elif unit == 'Fahrenheit':
            c = fahrenheit_to_celsius(temp_value)
            k = fahrenheit_to_kelvin(temp_value)
            result.set(f"Celsius: {c:.5f}\nKelvin: {k:.5f}")
        elif unit == 'Kelvin':
            c = kelvin_to_celsius(temp_value)
            f = kelvin_to_fahrenheit(temp_value)
            result.set(f"Celsius: {c:.5f}\nFahrenheit: {f:.5f}")
        else:
            messagebox.showerror("Error", "Invalid unit of temperature")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def create_gui():
    root = tk.Tk()
    root.title("Temperature Conversion")
    root.geometry("400x200")

    ttk.Label(root, text="Enter Temperature:").grid(column=0, row=0, padx=10, pady=10)
    global entry_value
    entry_value = ttk.Entry(root)
    entry_value.grid(column=1, row=0, padx=10, pady=10)

    ttk.Label(root, text="Select Unit:").grid(column=0, row=1, padx=10, pady=10)
    global combo_unit
    combo_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"])
    combo_unit.grid(column=1, row=1, padx=10, pady=10)
    combo_unit.current(0)  # set default value to Celsius

    convert_button = ttk.Button(root, text="Convert", command=convert_temperature)
    convert_button.grid(column=0, row=2, columnspan=2, padx=10, pady=10)

    global result
    result = tk.StringVar()
    ttk.Label(root, textvariable=result).grid(column=0, row=3, columnspan=2, padx=10, pady=10)

    root.mainloop()

create_gui()
