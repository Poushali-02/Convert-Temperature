# 🌡️ Temperature Converter 🌡️

## 📜 Description

This is a simple 🎨 GUI-based Temperature Converter built using 🐍 Python and 🖼️ Tkinter. The app allows users to input a temperature value and specify the unit (🌡️ °Celsius or 🌡️ °Fahrenheit), then converts it to the corresponding unit.

## ✨ Features

- 🖥️ User-friendly interface using Tkinter

- 🔢 Accepts temperature input

- 🔄 Converts between °C and °F

- ⚠️ Displays error messages for invalid inputs

## ⚙️ Requirements

- Ensure you have 🐍 Python installed. This script uses Tkinter, which comes pre-installed with Python.

## 🚀 Installation & Usage

- ⬇️ Download or clone the script.

- ▶️ Run the script using:

python convert.py

- ✏️ Enter the temperature in the input field.

- 🔤 Enter the unit (C or F).

- 🖱️ Click "Submit" to see the converted temperature.

## 🏗️ Code Structure

- root 🎭: Main application window

- Temperature 🌡️: Input field for temperature

- unit 🔤: Input field for unit selection

- get_Temp() 🔄: Function handling conversion logic

- result_label 📌: Displays the result

- 🔄 Conversion Logic

- If the unit is "Celsius" (C), it converts to Fahrenheit.

- If the unit is "Fahrenheit" (F), it converts to Celsius.

- ❌ Displays an error for invalid input.

# 📊 Example Usage

Input: 100
Unit: C
Output: 100.0°C = 212.0°F

Input: 32
Unit: F
Output: 32.0°F = 0.0°C

