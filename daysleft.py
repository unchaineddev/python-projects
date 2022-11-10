age = input("What is your current age? ")
age1 = int(age)

years_remaining = 100 - age1
days = years_remaining*365
weeks = years_remaining*52
months = years_remaining*12

message = f"You have {days} days, {weeks} weeks, and {months} months left."
print(message)




