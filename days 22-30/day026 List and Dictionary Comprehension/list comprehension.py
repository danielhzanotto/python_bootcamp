numbers = [1, 2, 3, 4]
new_list = [n + 1 for n in numbers]
print(new_list)


name = "Daniel"
letter_list = [letter for letter in name]
print(letter_list)

numbers = [n*2 for n in range(1, 5)]
print(numbers)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
upper_names = [name.upper() for name in names if len(name) > 4]
print(upper_names)

fibonacci = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n*n for n in fibonacci]
print(squared_numbers)
even_numbers = [n for n in fibonacci if n % 2 == 0]
print(even_numbers)
