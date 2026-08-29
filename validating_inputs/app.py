"""
Exercises for Programmers 57 Challenges to Develop Your Coding Skills
Exercise 27: Validating Inputs
"""
# Prompt user for input, if invalid it repeats
def get_input():
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        zip = input("Enter the ZIP code: ")
        emp_id = input("Enter an employee ID: ")
        return first_name, last_name, zip, emp_id

# Validating user inputs and printing in single output
def validateInput(first_name, last_name, zip, emp_id): 
        errors = []

        if len(first_name) == 0:
            errors.append("The first name must be filled in.")
        elif len(first_name) < 2:
            errors.append(f'"{first_name}" is not a valid first name. It is too short.')

        if len(last_name) == 0:
            errors.append("The last name must be filled in.")
        elif len(last_name) < 2:
            errors.append(f'"{last_name}" is not a valid last name. It is too short.')

        if not zip.isdigit():
            errors.append("The ZIP code must be numeric.")

        if len(emp_id) != 7 or not (emp_id[0:2].isalpha() and emp_id[2] == '-' and emp_id[3:].isdigit()):
            errors.append(f"{emp_id} is not a valid ID.")

        if errors:
            print("\n".join(errors))
        else:
            print("There were no errors found.")
        
# Run function
def run():
    first_name, last_name, zip, emp_id = get_input()
    validateInput(first_name, last_name, zip, emp_id)

run()