"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 18: Temperature Converter
"""

# To get user input on variables
def get_input(): 
    while True:
        unit = input("Press C to convert from Fahrenheit to Celsius.\nPress F to convert from Celsius to Fahrenheit.\n").upper()
        if unit in ["C", "F"]:
            break
        print("Invalid unit. Please enter C or F.")

    while True:
        try:
            if unit == "C":
                temperature = float(input("Please enter the temperature in Fahrenheit: "))
            elif unit == "F":
                temperature = float(input("Please enter the temperature in Celsius: "))
            return unit, temperature
        except ValueError:
            print("Invalid input! Please enter a numerical value.")

# Conditional statement on state, to determine conversion formula
def convert(unit, temperature):
    converted_temperature = 0
    if unit == "C":
        converted_temperature = (temperature-32) * (5/9)    
    elif unit == "F":
        converted_temperature = (temperature*1.8) + 32
    else: 
        print("Wrong input!")
    return converted_temperature

# Print output function 
def print_message(unit, converted_temperature):
    print(f"Your unit: {unit}")
    if unit == "C":
        unit = "Celsius"
    elif unit == "F":
        unit = "Fahrenheit"
    print(f"The temperature in {unit} is {converted_temperature:.2f}")

# Main run function
def run(): 
    unit, temperature = get_input()
    converted_temperature = convert(unit, temperature)
    print_message(unit, converted_temperature)

run()
