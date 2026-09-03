"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 29: Handling Bad Input
"""

# To get user input on return rate, and prints years taken to double investment
def run():
    while True:
        try: 
            return_rate = int(input("What is the rate of return? "))
            if return_rate <= 0:
                print("Sorry. That's not a valid input")
                continue
            break
        except ValueError:
            print("Sorry. That's not a valid input")

    years = 72/return_rate
    print(f"It will take {years} years to double your initial investment.")

run()
