import pandas
#TODO 1. Create a dictionary in this format:
data=pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
data_dict={
     row.letter:row.code for (index,row) in data.iterrows()
 }

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input=input("Enter word: ")
li=[]
for letter in user_input:
    li.append(data_dict[letter.upper()])

print(li)