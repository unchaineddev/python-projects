# write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print([value for value in a if value<5])


# Extras
# Ask the user for a number and return a list that contains only elements 
# from the original list a that are smaller than that number given by the user.

def smaller_than_input():
    number = int(input("Enter a number"))
    
    return [i for i in a if i < number]

print(smaller_than_input())


