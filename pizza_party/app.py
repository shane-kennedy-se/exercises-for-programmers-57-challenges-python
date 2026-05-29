"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 8: Pizza Party
"""

# Prompt for input
def get_input():
    people = int(input("How many people?"))
    pizza_amt = int(input("How many pizzas do you have?"))
    return people, pizza_amt

# Calculate pizza per person
def calculate(people, pizza_amt):
    average_slices = 8
    slices = pizza_amt*average_slices
    slices_per_person = slices // people
    leftover = slices % people
    return slices_per_person, leftover

# Print output
def print_output(people, pizza_amt, slices_per_person, leftover):
    print(f"{people} people with {pizza_amt} pizzas.")
    print(f"Each person gets {slices_per_person} pieces of pizza.")
    print(f"There are {leftover} leftover pieces.")

# Run function 
def run(): 
    people, pizza_amt = get_input()
    pizza_pieces, leftover = calculate(people, pizza_amt)
    print_output(people, pizza_amt, pizza_pieces, leftover)

run()