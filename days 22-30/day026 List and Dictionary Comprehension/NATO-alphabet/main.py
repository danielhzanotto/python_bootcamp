import pandas

nato_abc = pandas.read_csv(
    "/Users/Daniel/Documents/Phyton Bootcamp/days 22-30/day026 List and Dictionary Comprehension/NATO-alphabet/nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_abc.iterrows()}

name = input("Type your name: ").upper()
name_code = [nato_dict[letter] for letter in name]
print(name_code)
