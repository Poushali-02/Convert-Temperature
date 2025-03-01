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

# Result label (separate from heading)
result_label = tk.Label(root, text="", bg="#FFB4A2", font=("Arial", 12))
result_label.pack(pady=10)


def get_Temp():
    get = Temperature.get()
    type = unit.get().strip().lower()
    try:
        temp = float(get)
        if type.lower() in ["celsius", "c"]:
            tempC = temp
            tempF = ((tempC * 9.0) / 5.0) + 32.0
            result_label.config(text=f"{tempC}°C = {tempF}°F")

        elif type.lower() in ["fahrenheit", "f"]:
            tempF = temp
            tempC = (tempF - 32.0) * (5.0 / 9.0)
            result_label.config(text=f"{tempF}°F = {tempC}°C")
        else:
            result_label.config(text="Invalid unit! Use C or F.", fg="red")
    except:
        result_label.config(text="Please enter a valid number!")


button = tk.Button(root, text="Submit", bg="#FFB4A2", font = ("Arial", 12) ,command=get_Temp)
button.pack()

# this starts the program
root.mainloop()
