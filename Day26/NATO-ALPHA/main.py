import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

name = input("Enter a word: ")

#for (index, row) in data.iterrows():
#    print(row.letter)
# Create code dictionary from panda data frame created from csv
#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# create a list converting each letter of the input name to the code
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
codewords = [code_dict[letter.upper()] for letter in name]

print(codewords)
