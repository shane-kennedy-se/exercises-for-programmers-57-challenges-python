"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 12: Computing Simple Interest
"""

import math

# Prompt for user input
def get_input(): 
    principal = float(input("Enter the principal: "))
    interest_rate = float(input("Enter the rate of interest(as %): "))
    years = float(input("Enter the number of years: "))
    return principal, interest_rate, years

# Calculate interest with formula
def calculate_interest(principal, interest_rate, years):
    interest = (math.ceil(principal*(1+(interest_rate/100)*years)*100))/100
    return interest

# Print output
def print_output(interest_rate, years, interest):
    print(f"After {years} years at {interest_rate:.2f}%, the investment will be worth ${interest:.2f}")

# Run function
def run():
    principal, interest_rate, years = get_input()
    interest = calculate_interest(principal, interest_rate, years)
    print_output(interest_rate, years, interest)

run()