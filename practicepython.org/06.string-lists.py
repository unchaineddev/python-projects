# Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

def check_palindrome():
    user_input = input("Enter a string: ").lower()
    reverse_string = user_input[::-1]

    return f"{user_input} is a palindrome" if user_input == reverse_string else f"{user_input} is not a palindrome" 


print(check_palindrome())
