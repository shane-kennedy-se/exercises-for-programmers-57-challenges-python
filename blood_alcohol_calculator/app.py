"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 17: Blood Alcohol Calculator
"""

# Get user input
def get_input():
    try: 
        weight = float(input("What is your weight (in pounds)? "))
    except ValueError: 
        print("Invalid weight")

    gender = input("What is your gender (M or F)? ")

    try: 
        no_of_drinks = float(input("Number of drinks? "))
    except ValueError:
        print ("Invalid amount")

    try:    
        volume_drinks = float(input("What is the volume of the drinks consumed? in ounces "))
    except ValueError:
        print("Invalid volume")

    try: 
        time_last_drink = float(input("What is the amount of time since your last drink? in hours "))
    except ValueError: 
        print("Invalid amount of hours")
    
    return weight, gender, no_of_drinks, volume_drinks, time_last_drink

# Calculate blood alcohol content
def calculate(weight, gender, no_of_drinks, volume_drinks, time_last_drink):

    if gender in ("M", "m"):
        alcohol_ratio = 0.73
    elif gender in ("F", "f"):
        alcohol_ratio = 0.66
    else :
        print("Invalid input")
    abv = 0.05
    alcohol = volume_drinks*abv*no_of_drinks

    blood_alcohol = (alcohol * 5.14/(weight * alcohol_ratio)) - (0.015 * time_last_drink)

    return max(0.0, round(blood_alcohol, 2))

# Print blood alcohol content and status
def print_output(blood_alcohol): 
    print(f"Your BAC is {blood_alcohol:.2f}")

    if blood_alcohol >= 0.08 :
        print("It is not legal for you to drive.")
    else:
        print("It is legal for you to drive.")

# Main run function
def run ():
    weight, gender, no_of_drinks, volume_drinks, time_last_drink = get_input()
    blood_alcohol = calculate(weight, gender, no_of_drinks, volume_drinks, time_last_drink)
    print_output(blood_alcohol)

run()