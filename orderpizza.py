print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_chicken = input("Do you want chicken? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


bill = 0

if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    size == 'L'
    bill += 25

if add_chicken == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1


print(f"Your final bill is: {bill}")
