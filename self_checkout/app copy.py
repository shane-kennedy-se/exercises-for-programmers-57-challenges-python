"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 10: Self checkout
"""
import math

# Prompt user for input, if invalid it repeats
def get_input():
    while(True):
        try: 
            length = int(input("What is the length of the room in feet?"))
            width = int(input("What is the width of the room in feet?"))
            return length, width
        except(ValueError):
            print("Invalid numeric")
        continue

# Calculate total area and gallons required to paint everything, rounding up
def calculate(length, width): 
    total_area = length * width
    gallons_required = math.ceil(total_area/350)
    return total_area, gallons_required

# Print output
def print_output(total_area, gallons_required):
    print(f"You will need to purchase {gallons_required} gallons of paint to cover {total_area} square feet.")

# Run function
def run():
    length, width = get_input()
    total_area, gallons_required = calculate(length, width)
    print_output(total_area, gallons_required)

run()