"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 24: Anagram Checker
"""

# To get user input on variables
def get_input():
    print("Enter two strings and I'll tell you if they are anagrams")
    while True:
        try: 
            str1 = input("Enter the first string: ")
            str2 = input("Enter the second string: ")
            return str1, str2
        except ValueError:
            print("Invalid input.")

# Conditional statement to check if length the same, then sort by letters if they match
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False
    if sorted(str1.lower()) == sorted(str2.lower()):
        return True 
    return False
 
# Print output function 
def print_message(is_anagram, str1, str2):
    if is_anagram:
        print(f'"{str1}" and "{str2}" are anagrams.')
    else:
        print(f'"{str1}" and "{str2}" are not anagrams.')

# Main run function
def run(): 
    str1, str2 = get_input()
    result = is_anagram(str1, str2)
    print_message(result, str1, str2)

run()
