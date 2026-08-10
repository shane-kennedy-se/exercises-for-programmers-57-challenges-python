"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 14: Tax Calculator
"""

# To get user input on variables
def get_input(): 
    order_amt = input("What is the order amount?")
    state = input("What is the state?")
    return order_amt, state

# Conditional statement on state, to determine tax rate
def calculate(order_amt, state):
    subtotal = float(order_amt)
    tax = 0.0

    if state == "WI":
        tax = subtotal * 0.055

    total = subtotal + tax
    return subtotal, tax, total

# Print output function 
def print_message(state, subtotal, tax, total):
    print(f"The subtotal is ${subtotal:.2f}")
    if state == "WI":
        print(f"The tax is ${tax:.2f}")
    print(f"The total is ${total:.2f}")

# Main run function
def run(): 
    order_amt, state = get_input()
    subtotal, tax, total = calculate(order_amt, state)
    print_message(state, subtotal, tax, total)

run()
