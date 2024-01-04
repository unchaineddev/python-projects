# Write a program (using functions!) that asks the user for a long string
# containing multiple words. Print back to the user the same string, 
# except with the words in backwards order.


ask_str = input("Enter a string to reverse the order: ")

def reverse_word(ask_str):
    word = ask_str.split(" ")
    return ' '.join(reversed(word))

#res = reverse_word(ask_str)
# print(res)


word = input('Enter a sentence: ')
def reversing_word(word):
    reversed_word = "" 

    for i in word.split(" "):
        reversed_word = word[-i] + " "
    return reversed_word


reversing_word(word)

