"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 6: Retirement calculator
"""

from datetime import date

# Input function for age and retirement age
def get_input():
    current_age = int(input("What is your current age?\n"))
    retirement_age = int(input("At what age would you like to retire?\n"))
    return current_age, retirement_age

# Computations for years left and retirement year 
def calculate(current_age, retirement_age):
    years_left = retirement_age - current_age
    current_year = date.today().year
    retirement_year = current_year + years_left
    return years_left, current_year, retirement_year     

# Print output message, conditional
def print_message(years_left, current_year, retirement_year):
    if years_left > 0 :
        print(f"You have {years_left} years until you can retire \nIt's {current_year}, so you can retire in {retirement_year}.")
    else :
        print("You can retire now!")

# Run execution
def run():
    current_age, retirement_age = get_input()
    years_left, current_year, retirement_year = calculate(current_age, retirement_age)
    print_message (years_left, current_year, retirement_year)

run()