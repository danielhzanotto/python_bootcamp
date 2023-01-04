import pandas

nato_abc = pandas.read_csv(
    "days 22-30/day026 List and Dictionary Comprehension/NATO-alphabet/nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_abc.iterrows()}


def generate_phonetic():
    name = input("Type your name: ").upper()
    try:
        name_code = [nato_dict[letter] for letter in name]
    except KeyError:
        print("Please use only alphabet letters")
        generate_phonetic()
    else:
        print(name_code)


generate_phonetic()
