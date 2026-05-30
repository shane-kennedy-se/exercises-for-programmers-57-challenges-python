

# Tax rate constant
tax_rate = 0.055

# Prompt user for input on item prices and quantity
def get_input(num_items=3):  
    items = []
    for i in range(1, num_items + 1):
        while True:
            try:
                price = float(input(f"Enter the price of item {i}:"))
                quantity = int(input(f"Enter the quantity of item {i}:"))
            except ValueError:
                print("Invalid input. Enter a number for price and an integer for quantity.")
                continue
            items.append({"price": price, "quantity":quantity})
            break
    return items

# Calculate subtotal, tax, total
def calculate(items): 
    sub_total = sum(item["price"] * item["quantity"] for item in items)
    tax_amt = sub_total * tax_rate
    total_amt = sub_total + tax_amt
    return sub_total, tax_amt, total_amt

# Print output  
def print_output (sub_total, tax_amt, total_amt):
    print(f"Subtotal: ${sub_total:.2f}\nTax: ${tax_amt:.2f}\nTotal: ${total_amt:.2f}")

# Run function
def run(): 
    cart = get_input()
    sub_total, tax_amt, total_amt = calculate(cart)
    print_output(sub_total, tax_amt, total_amt)
run()