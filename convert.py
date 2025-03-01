# tkinter added as GUI
import tkinter as tk

# this creates the main window
root = tk.Tk()

root.title("Temperature Converter")
root.geometry("500x500")
root.configure(bg="#FFCDB2")

# Heading
heading = tk.Label(root, text="Enter temperature", fg="white", bg="#B5828C", font=("Arial", 12))
heading.pack()

# Get temperature
Temperature = tk.Entry(root, width=40, bg="white", font=("Arial", 12))
Temperature.pack(pady=10)

# unit heading
command = tk.Label(root, text="Enter unit", fg="white", bg="#B5828C", font=("Arial", 12))
command.pack()

# get Unit
unit = tk.Entry(root, width=40, bg="white", font=("Arial", 12))
unit.pack(pady=10)

# unit heading
convertTo = tk.Label(root, text="Enter in which unit to convert", fg="white", bg="#B5828C", font=("Arial", 12))
convertTo.pack()

# get Unit
toUnit = tk.Entry(root, width=40, bg="white", font=("Arial", 12))
toUnit.pack(pady=10)

# Result label (separate from heading)
result_label = tk.Label(root, text="", bg="#FFB4A2", font=("Arial", 12))
result_label.pack(pady=10)


def get_Temp():
    get = Temperature.get()
    from_unit = unit.get().strip().lower()
    to_unit = toUnit.get().strip().lower()
    
    try:
        temp = float(get)

        if from_unit in ["celsius", "c"] and to_unit in ["kelvin", "k"]:
            tempK = temp + 273.15  # Celsius to Kelvin
            result_label.config(text=f"{temp}°C = {tempK} K")

        elif from_unit in ["celsius", "c"] and to_unit in ["fahrenheit", "f"]:
            tempF = ((9.0 / 5.0) * temp) + 32.0  # Celsius to Fahrenheit
            result_label.config(text=f"{temp}°C = {tempF}°F")

        elif from_unit in ["fahrenheit", "f"] and to_unit in ["celsius", "c"]:
            tempC = (temp - 32.0) * (5.0 / 9.0)  # Fahrenheit to Celsius
            result_label.config(text=f"{temp}°F = {tempC}°C")

        elif from_unit in ["fahrenheit", "f"] and to_unit in ["kelvin", "k"]:
            tempK = (temp - 32.0) * (5.0 / 9.0) + 273.15  # Fahrenheit to Kelvin
            result_label.config(text=f"{temp}°F = {tempK} K")

        elif from_unit in ["kelvin", "k"] and to_unit in ["celsius", "c"]:
            tempC = temp - 273.15  # Kelvin to Celsius
            result_label.config(text=f"{temp} K = {tempC}°C")

        elif from_unit in ["kelvin", "k"] and to_unit in ["fahrenheit", "f"]:
            tempF = (temp - 273.15) * (9.0 / 5.0) + 32.0  # Kelvin to Fahrenheit
            result_label.config(text=f"{temp} K = {tempF}°F")

        else:
            result_label.config(text="Invalid unit! Use C, F, or K.", fg="red")

    except ValueError:
        result_label.config(text="Please enter a valid number!", fg="red")


# Submit button
button = tk.Button(root, text="Submit", bg="#FFB4A2", font=("Arial", 12), command=get_Temp)
button.pack()

# this starts the program
root.mainloop()
