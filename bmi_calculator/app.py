"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 19: BMI Calculator
"""

# To get user input on variables
def get_input():
    while True:
        try: 
            weight = float(input("What is your weight? (in pounds) "))
            height = float(input("What is your height? (in inches) "))
            return weight, height
        except ValueError:
            print("Invalid input. Please enter numerical values.")

# Conditional statement on state, to determine status
def calculate(weight, height):
    bmi = (weight/(height*height)) * 703
    if bmi <= 18:
        status = "Underweight"       
    elif 18 < bmi < 25: 
        status = "Normal"
    elif bmi >= 25: 
        status = "Overweight"
    return bmi, status


# Print output function 
def print_message(bmi, status):
    print(f"Your BMI is {bmi:.2f}")
    if status == "Normal":
        print("You are within the ideal weight range.")
    elif status == "Underweight":
        print("Eat more.")
    elif status == "Overweight":
        print("You are overweight. You should see your doctor.")

# Main run function
def run(): 
    weight, height = get_input()
    bmi, status = calculate(weight, height)
    print_message(bmi, status)

run()
