"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 11: Currency conversion
"""

# Prompt input for euros and exchange rate
def get_input():
    amt_from = float(input("How many euros are you exchanging?"))
    exchange_rate = float(input("What is the exchange rate in euros per dollars?"))
    return amt_from, exchange_rate

# Convert euros to dollars
def convert(amt_from, exchange_rate):
     amt_to = (amt_from*exchange_rate)
     return amt_to

# Print output 
def print_output(amt_from, exchange_rate, amt_to):
     print(f"{amt_from:.2f} eueros at the exchange rate of {exchange_rate:.2f} is {amt_to:.2f} U.S. dollars.")

# Run function
def run(): 
    amt_from, exchange_rate = get_input()
    amt_to = convert(amt_from, exchange_rate)
    print_output(amt_from, exchange_rate, amt_to)

run()
