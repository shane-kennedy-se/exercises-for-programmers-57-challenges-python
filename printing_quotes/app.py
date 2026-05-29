"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 3: Printing Quotes
"""

# Get quote and author
def get_input() :
    quote = input("What is the quote?")
    author = input("Who said it? ")
    return quote,author

# Print quote and author with escape characters
def print_message(quote,author):
    print(f"{author} says, \"{quote}\"")

def run():
    quote, author = get_input()
    print_message(quote,author)

run()