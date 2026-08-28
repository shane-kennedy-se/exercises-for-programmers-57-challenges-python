"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 26: Months to pay off a credit card
"""

import math

# To get user input on variables
def get_input(): 
    balance = float(input("What is your balance? "))
    apr = float(input("What is the APR on the card (as a percent)? "))
    monthly_payment = float(input("What is the monthly payment you can make? "))
    return balance, apr, monthly_payment

# Function to calculate months until paid off using formula
def calculateMonthsUntilPaidOff(balance, apr, monthly_payment):
    i = (apr / 100) / 365
    b = balance 
    p = monthly_payment

    numerator = math.log(1 + (b/p) * (1 - pow(1 + i, 30)))
    denominator = math.log(1 + i)

    balance_months = -(1/30) * numerator/denominator
    return math.ceil(balance_months)

# Print output function 
def print_message(balance_months):
    print(f"It will take you {balance_months} months to pay off this card.")

# Main run function
def run(): 
    balance, apr, monthly_payment = get_input()
    balance_months = calculateMonthsUntilPaidOff(balance, apr, monthly_payment)
    print_message(balance_months)

run()
