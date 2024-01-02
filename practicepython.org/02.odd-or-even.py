# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2

number = int(input("Enter a number: "))

# Method 1 
print("Even!" if number % 2 == 0 else "Odd!")

# Method 2

if number % 2 == 0:
    print("Even!")
else:
    print("Odd!")

