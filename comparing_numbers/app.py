"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 22: Comparing Numbers
"""

# To get user input on variables
def get_input():
    while True:
        try: 
            first_num = int(input("Enter the first number: "))
            second_num = int(input("Enter the second number: "))
            third_num = int(input("Enter the third number: "))
            return first_num, second_num, third_num
        except ValueError:
            print("Invalid input.")

# Conditional statement on number values, to get the largest number
def get_largest_number(first_num, second_num, third_num):
    if first_num > second_num and first_num > third_num:
        largest_number = first_num
    elif second_num > first_num and second_num > third_num :
        largest_number = second_num
    elif third_num > first_num and third_num > second_num:
        largest_number = third_num
    return largest_number

# Print output function 
def print_message(largest_number):
    print(f"The largest number is {largest_number}")

# Main run function
def run(): 
    first_num, second_num, third_num = get_input()
    largest_number = get_largest_number(first_num, second_num, third_num)
    print_message(largest_number)
    
run()
