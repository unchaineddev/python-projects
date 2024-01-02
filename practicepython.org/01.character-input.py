# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 
# Note: for this exercise, the expectation is that you explicitly write out the year 
# (and therefore be out of date the next year).


from datetime import datetime

current_year = datetime.now().year

user_name = input("Enter your name: ").title()
age = int(input("Enter your age: "))

final_year = current_year + (100 - age)

print(f'{user_name}, You will be 100 years old in the year {final_year}')

# Extras

random_number = int(input("Enter a random number now or press 0 to exit: "))

if random_number != 0:
    print(random_number * str(final_year))
else:
    exit()

