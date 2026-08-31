"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 28: Adding Numbers
"""

# To get user input on number of prompts, and values
def run():
    amount = int(input("How many numbers to add? "))
    i = 1
    total = 0
    while i <= amount:
        try:
            num = int(input("Enter a number: "))
            total = total + num
            i = i + 1
        except ValueError:
            i = i + 1

    print(f"The total is {total}")

run()
