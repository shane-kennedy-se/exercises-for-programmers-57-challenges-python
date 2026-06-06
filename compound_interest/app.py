"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 13: Determining compound interest
"""

# Get user input
def get_input(): 
    principal = float(input("What is the principal amount?"))
    rate = float(input("What is the rate? in %"))
    years = float(input("What is the number of years?"))
    compound_rate = float(input("What is the number of times the interest is compounded per year?"))
    return principal, rate, years, compound_rate

# Calculate logic for compounded amount 
def calculate(principal, rate, years, compound_rate):
    rate = rate / 100
    amount = principal * (1 + (rate/compound_rate)) ** (compound_rate * years)
    return amount

# Print message
def print_output(principal, rate, years, compound_rate, amount):
    print(f"${principal} invested at {rate} for {years} years compounded {compound_rate} times per year is amount ${amount:2f}")

# Run function
def run(): 
    principal, rate, years, compound_rate = get_input()
    amount = calculate(principal, rate, years, compound_rate)
    print_output(principal, rate, years, compound_rate, amount)

run()