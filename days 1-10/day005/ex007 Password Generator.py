import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for n in range(1, nr_letters + 1):
    password.append(letters[random.randint(0, len(letters)-1)])
    # password += random.choice(letters)

for n in range(1, nr_symbols + 1):
    password.append(numbers[random.randint(0, len(numbers)-1)])
    # password += random.choice(numbers)

for n in range(1, nr_numbers + 1):
    password.append(symbols[random.randint(0, len(symbols)-1)])
    # password += random.choice(symbols)

random.shuffle(password)

#pass_final = "".join(password)
pass_final = ""
for i in password:
    pass_final += i

print(pass_final)
