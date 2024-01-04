# Write a password generator in Python. Be creative with how you generate passwords - 
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks 
# for a new password. Include your run-time code in a main method.

# Extra: Ask the user how strong they want their password to be. 
# For weak passwords, pick a word or two from a list.


# My Method
import random

def main():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    n = int(input("Enter a length for your password: "))
    passwd = random.sample(s, n)
    return "".join(passwd)


if __name__ == "__main__":
    res = main()
    print(res)


# Method 2 - found in S.O
# https://stackoverflow.com/questions/65689199/how-to-generate-random-password-in-python

import string
import secrets

symbols = ['*', '%', '£'] # Can add more

password = ""
for _ in range(9):
    password += secrets.choice(string.ascii_lowercase)
password += secrets.choice(string.ascii_uppercase)
password += secrets.choice(string.digits)
password += secrets.choice(symbols)

print("Your password is %s" % password)