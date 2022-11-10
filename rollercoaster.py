print ("Welcome to the Python Roller coaster ride!")

height = int (input("Enter your height in cm: "))

if height > 120:
    print ("You can ride the roller coaster!! ")
    age = int (input("Enter your age: "))
    bill = 0    
    if age > 18:
        print("Tickets for adults is $12")
        bill += 12
    elif age < 12:
        print("Tickets for Kids is $5 ")
        bill += 5
    else: 
        bill += 7
        print ("Tickets for Teens is $7 ")

    photos = input ("Do you want to click photos: Y or N? ")
    if photos == 'Y':
        bill += 3
    print (f"Total Bill is {bill} ")

else:
    print ("Sorry ! You cannot ride the roller coaster!")

    
