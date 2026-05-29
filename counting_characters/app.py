"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 2: Counting characters
"""

# Prompt user for string input
def get_input():
    input_str = input("What is the input string?")
    return input_str
   
# Print output 
def print_message(input_str):
    print(f'{input_str} has {len(input_str)} characters.')

# Run function
def run() : 
    input_str = get_input()
    if len(input_str) > 0: 
        print_message(input_str)
    else: 
        print ("Valid input required.")

run()