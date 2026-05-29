"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 6: Area of a Rectangular Room
"""

# Constant declared
constant = 0.09290304

# Prompt for user input
def get_input():
    try: 
        length = int(input("What is the length of the room in feet?"))
        width = int(input("What is the width of the room in feet?"))
        return length, width
    except(ValueError):
        print("Invalid numeric")

# Calculate area
def calculate(length, width):
    area_feet = length * width
    area_square_meters = area_feet * constant
    return area_feet, area_square_meters

# Print output
def print_output(length, width, area_feet, area_square_meters):
    print(f"You entered dimensions of {length} feet by {width} feet")
    print(f"The area is\n{area_feet} square feet\n{area_square_meters} square meters")

# Run 
def run():
    length, width = get_input()
    area_feet, area_square_meters = calculate(length, width)
    print_output(length, width, area_feet, area_square_meters)

run()
