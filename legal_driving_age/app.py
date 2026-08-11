"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 16: Legal driving age
"""

# Get user input for age with try/catch
def get_input(): 
    while True:
        try: 
            age = int(input("What is your age?"))

            if age <= 0:
                print("Error: Please enter a valid age. Age cannot be negative.") 
                continue

            return age
        except ValueError:
            print("Error: Please enter a valid age. Input must be a whole number.")     

# Validate user age using ternary operator
def validate(age): 
    status = "You are old enough to legally drive." if age >= 16 else "You are not old enough to legally drive."
    return status

# Print output message
def print_output(status):
    print(status)

# Main run method
def run(): 
        age = get_input()
        status = validate(age)
        print_output(status)          

run()
