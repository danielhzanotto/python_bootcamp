import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

# Loop through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    print(value)

################################################

student_dframe = pandas.DataFrame(student_dict)

# Loop through dataframe columns:
for (key, value) in student_dframe.items():
    print(key)


# Loop through dataframe rows:
for (index, row) in student_dframe.iterrows():
    print(row.student, row.score)
