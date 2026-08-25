"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 25: Password Strength Indicator
"""

# To get user input 
def get_input():
    password = input("What is your password? ")
    return password

# Password validation condtionals
def passwordValidator(password): 
    length = len(password)
    has_letters = any(c.isalpha() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if length >= 8 and has_letters and has_digits and has_special:
        return 4
    elif length >= 8 and has_letters and has_digits:
        return 3
    elif length < 8 and password.isalpha():
        return 2
    elif length < 8 and password.isdigit():
        return 1
    else:
        return 0

# Main run function
def run():
    password = get_input()
    levels = ["an unclassified", "a very weak", "a weak", "a strong", "a very strong"]
    status = passwordValidator(password)
    print(f"The password {password} is {levels[status]} password.")

run()

