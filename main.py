student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(row.score)
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alpha_df = pandas.read_csv("nato_phonetic_alphabet.csv")
# for (index, row) in alpha_df.iterrows():
#     print(row.code)

new_dict = {row.letter: row.code for (index, row) in alpha_df.iterrows()}
# print(new_dict.items)

# 2. Create a list of the phonetic code words from a word that the user inputs.

word = (input("Enter a word: ")).upper()
output_list = [new_dict[letter] for letter in word]
print(output_list)
# letters = [letter for letter in word]
# code_words = []
# for letter in letters:
#     code_words.append(new_dict[letter])
# print(code_words)



