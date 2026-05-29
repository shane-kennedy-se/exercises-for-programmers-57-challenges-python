"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 1: Saying Hello
"""

def get_name():
    while True:
        print(f"What is your name?")
        name = input()
        return name

def print_greeting(name): 
    print (f"Hello {name} nice to meet you!")

def run():
    name = get_name()
    print_greeting(name)

run()