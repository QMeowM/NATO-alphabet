import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dic = {row.letter:row.code for (index, row) in data.iterrows()}
# print(dic)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

quest = input("What's the word? : ").upper()
result = [dic[i] for i in quest]
print(result)
