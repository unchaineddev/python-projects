# Sample Dictionary 
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

# reading csv file from pandas
data = pandas.read_csv("./nato_phonetic_alphabet.csv")
#print(data.to_dict())

# Creating Dict in form of K,V pair
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def phonetic():
    word = input("enter a word: ").upper()
    try:
        output = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only alphabets are allowed!")
        phonetic()
    else:
        print(output)

phonetic()
