# tkinter added as GUI
import tkinter as tk

# this creates the main window
root = tk.Tk()

root.title("Temperature Converter")
root.geometry("500x500")
root.configure(bg="#FFCDB2")

# Heading
heading = tk.Label(root, text="Enter temperature",fg = "white", bg="#B5828C", font=("Arial", 12))
heading.pack()

# Get temperature
Temperature = tk.Entry(root, width=40, bg="white", font=("Arial", 12))
Temperature.pack(pady=10)

# unit heading
command = tk.Label(root, text="Enter unit",fg = "white", bg="#B5828C", font=("Arial", 12))
command.pack()

# get Unit
unit = tk.Entry(root, width=40, bg="white", font=("Arial", 12))
unit.pack(pady=10)

# unit heading
convertTo = tk.Label(root, text="Enter in which unit to convert",fg = "white", bg="#B5828C", font=("Arial", 12))
convertTo.pack()

# get Unit
toUnit = tk.Entry(root, width=40, bg="white", font=("Arial", 12))
toUnit.pack(pady=10)

# Result label (separate from heading)
result_label = tk.Label(root, text="", bg="#FFB4A2", font=("Arial", 12))
result_label.pack(pady=10)


def get_Temp():
    get = Temperature.get()
    type = unit.get().strip().lower()
    toType = toUnit.get().strip().lower()
    try:
        temp = float(get)
        if type.lower() in ["celsius", "c"] and toType.lower() in ["kelvin", "k"]:
            tempC = temp #celcius to kelvin
            tempK = tempC + 273
            result_label.config(text=f"{tempC}°C = {tempK} K")
            
        elif type.lower() in ["celcius", "c"] and toType.lower() in ["fahrenheit", "f"]:
            tempC = temp #celcius to fahrenheit
            tempF = ((9.0 / 5.0) * (tempF)) + 32.0 
            result_label.config(text=f"{tempC}°C = {tempF}°F")
          
        elif type.lower() in ["fahrenheit", "f"] and toType.lower() in ["celcius", "c"]:
            tempF = temp #fahrenheit to celcius
            tempC = (tempF - 32.0) * (5.0 / 9.0)
            result_label.config(text=f"{tempF}°F = {tempC}°C")
            
        elif type.lower() in ["fahrenheit", "f"] and toType.lower() in ["kelvin", "k"]:
            tempF = temp #fahrenheit to kelvin
            tempC = (tempF - 32.0) * (5.0 / 9.0)
            tempK = tempC + 273
            result_label.config(text=f"{tempF}°F = {tempK} K")
          
        elif type.lower() in ["kelvin", "k"] and toType.lower() in ["celcius", "c"]:
            tempK = temp #kelvin to celcius
            tempC = tempK - 273
            result_label.config(text=f"{tempK} K = {tempC}°C")
              
        elif type.lower() in ["kelvin", "k"] and toType.lower() in ["fahrenheit", "f"]:
            tempK = temp #kelvin to fahrenheit
            tempC = tempK - 273
            result_label.config(text=f"{tempK} K = {tempC}°C")
        
        else:
            result_label.config(text="Invalid unit! Use C or F or K.", fg="red")
    except:
        result_label.config(text="Please enter a valid number!")


button = tk.Button(root, text="Submit", bg="#FFB4A2", font = ("Arial", 12) ,command=get_Temp)
button.pack()

# this starts the program
root.mainloop()
