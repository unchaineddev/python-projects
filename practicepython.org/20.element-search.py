# Write a function that takes an ordered list of numbers 
# (a list where the elements are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list and 
# returns (then prints) an appropriate boolean.


def element_search(my_list, n):
    for ele in my_list:
        if n in my_list:
            return True
        else:
            return False


res = element_search([1, 2, 3, 4, 5], n =3)
print(res)
