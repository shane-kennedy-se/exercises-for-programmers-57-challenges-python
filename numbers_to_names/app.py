"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 21: Numbers to Names
"""

# To get user input on variables
def get_input():
    while True:
        try: 
            month = int(input("Please enter the number of the month: "))
            return month
        except ValueError:
            print("Invalid input.")

# Conditional statement on month value, to get month name
def get_month_name(month):
    match month: 
        case 1:
            month_name = "January"
        case 2:
            month_name = "February"
        case 3:
            month_name = "March"
        case 4:
            month_name = "April"
        case 5:
            month_name = "May"
        case 6:
            month_name = "June"
        case 7:
            month_name = "July"
        case 8:
            month_name = "August"
        case 9:
            month_name = "September"
        case 10:
            month_name = "October"
        case 11:
            month_name = "November"
        case 12: 
            month_name = "December"
        case _:
            month_name = ""
    return month_name

# Print output function 
def print_message(month, month_name):
    if 1 <= month <= 12:
        print(f"The name of the month is {month_name}")
    else:
        print("The month must be between 1 and 12")

# Main run function
def run(): 
    month = get_input()
    month_name = get_month_name(month)
    print_message(month, month_name)

run()
