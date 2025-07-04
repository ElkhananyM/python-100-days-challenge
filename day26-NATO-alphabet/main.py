# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetics_dict = {row["letter"]:row.code for (index, row) in data.iterrows()}
# phonetics_dict = {row.letter:row.code for row in data.itertuples(index=False)}
print(phonetics_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Enter a word: ").upper()
phonetics_list = [phonetics_dict[char] for char in user_word]
print(phonetics_list)