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


word = input("enter a word: ").upper()

output = [phonetic_dict[letter] for letter in word]
print(output)
