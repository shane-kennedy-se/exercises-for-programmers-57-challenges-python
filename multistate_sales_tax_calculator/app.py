"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 20: Multistate Sales Tax Calculator
"""

# To get user input on variables
def get_input():
    while True:
        try: 
            order_amt = int(input("What is the order amount? "))
            state = input("What state do you live in? ").upper()
            county = ""
            if state == "WISCONSIN" or state == "WI":
                county = input("What county do you live in? ").upper()
            return order_amt, state, county
        except ValueError:
            print("Invalid input.")

# Conditional statement on state, to determine tax rate
def calculate(order_amt, state, county):
    if state == "WISCONSIN" or state == "WI":
        tax_rate = 0.05
        if county == "EAU CLAIRE":
            tax_rate = tax_rate + 0.005
        elif county == "DUNN":
            tax_rate = tax_rate + 0.004
    elif state == "ILLINOIS" or state == "IL":
        tax_rate = 0.08
    else: 
        tax_rate = 0
    sales_tax = tax_rate * order_amt
    total = order_amt + sales_tax
    return sales_tax, total

# Print output function 
def print_message(state, sales_tax, total):
    if state == "WISCONSIN" or state == "WI" or state == "ILLINOIS" or state == "IL":
        print(f"The tax is ${sales_tax:.2f}.")
    print(f"The total is ${total:.2f}.")

# Main run function
def run(): 
    order_amt, state, county = get_input()
    sales_tax, total = calculate(order_amt, state, county)
    print_message(state, sales_tax, total)

run()
