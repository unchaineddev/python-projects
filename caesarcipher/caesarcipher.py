# Caesar Cipher 

# Added alphabets twice to avoid index error. example: zebra

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

   
# defining caesar function with start text, the shift amount and the direction
def caesar(start_text,shift_amount,cipher_direction):

    # creating end_text to contrast to the start_text
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    
    # looping through index() function to check the word

    for i in start_text:
        if i in alphabet:
            pos = alphabet.index(i)
            new_pos = pos + shift_amount
            end_text += alphabet[new_pos]

# If user enters a space
        else:
            end_text += i
    print(f"The {direction}d text is {end_text}")


from art import cs

print(cs)

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
        
    shift = shift % 26 

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


    result = input("Type Y to continue or N to exit: ").lower()
    if result == "n":
        should_continue = False
        print("Thank you, see you laters")




#    def encrypt(plain_text,shift_amount):
#        cipher_text = ""
#        for i in plain_text:
#    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#            pos = alphabet.index(i)
#            new_pos = pos + shift_amount
#            new_letter = alphabet[new_pos]
#            cipher_text += new_letter
#        print(f"The new encode text is {cipher_text}")
#
#    def decrypt(cipher_text,shift_amount):
#        plain_text = ""
#        for i in cipher_text:
#            pos = alphabet.index(i)
#            new_pos = pos - shift_amount
#            plain_text += alphabet[new_pos]
#        print(f"The new decoded text is {plain_text}")
#
#    if direction == "encode":
#        encrypt(plain_text=text, shift_amount=shift)
#    elif direction == "decode":
#        decrypt(cipher_text=text, shift_amount=shift)

