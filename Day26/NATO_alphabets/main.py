import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
dict1 = {row.letter : row.code for (index, row) in data.iterrows()}
def generate_phonetic():
    user_input = input("Enter a code: ").upper()
    try:
        output = [dict1[i] for i in user_input]
    except KeyError:
        print("Please enter alphabets only.")
        generate_phonetic()
    else:
        print(output)
generate_phonetic()