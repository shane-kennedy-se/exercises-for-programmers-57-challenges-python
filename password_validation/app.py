"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 15: Password Validation
"""

import getpass

# To get user input
def get_input():
    username = input("What is your username?") 
    password = getpass.getpass("What is the password?")
    return username, password

# Validation function matching username and password
def validate(username, password): 
    # Dictionary for username and passwords
    user_credentials = {
        "shane": "abc$123",
        "admin": "admin"
    }  

    # Get password based on username
    stored_password = user_credentials.get(username)

    # Conditional for username and password validation
    if stored_password is not None and stored_password == password:
        print(f"Welcome, {username}!")
    else: 
        print("I don't know you.")

# Main run function 
def run():
    username, password = get_input()
    validate(username, password)

run()