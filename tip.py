print("Welcome to the Tip Calculator!")

totalbill = float(input("Enter the total amount of the bill:$ "))
people = int(input("Enter the number of people you want to split the total bill with "))
perc = float(input("Enter the percentage split of the bill: "))

split = totalbill/people
total = split + (totalbill*perc)/(100*people)
final = round(total,2)

print(f"Each person has to pay: ${final}")
