"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 5: Simple Math
"""

# Get user input in int format 
def get_input(): 
    try:
        first_num = int(input("What is the first number? "))
        second_num = int(input("What is the second number? "))
        return first_num, second_num
    except ValueError:
        print("Invalid input! Please enter a whole number.")
        

# Calculation processing
def calculate(first_num, second_num): 
    sum = first_num + second_num
    diff = first_num - second_num
    multiply = first_num * second_num
    divide = first_num / second_num
    return sum, diff, multiply, divide

# Print output with linebreaks
def print_message(first_num, second_num, sum, diff, multiply, divide): 
    print(f"{first_num} + {second_num} = {sum}\n{first_num} - {second_num} = {diff}\n{first_num} * {second_num} = {multiply}\n{first_num} / {second_num} = {divide}")

# Declaring main method
def run(): 
    first_num, second_num = get_input()
    sum, diff, multiply, divide = calculate(first_num, second_num)
    print_message(first_num, second_num, sum, diff, multiply, divide)

run()
