"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 4: Mad lib
"""

# Prompt for user input
def get_input():
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter a adjective: ")
    adverb = input("Enter a adverb: ")
    return noun,verb,adjective,adverb

# Print output
def print_message(noun,verb,adjective,adverb):
    print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")

# Run function
def run():
    noun,verb,adjective,adverb = get_input()
    print_message(noun,verb,adjective,adverb)

run()