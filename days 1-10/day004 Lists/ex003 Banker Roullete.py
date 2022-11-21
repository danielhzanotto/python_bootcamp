import random

print("Welcome to the Banker Roullete")

names = []

print("Please add a name to the list")
names.append(input())

print("Would you like to add another name to the list? Y or N")
cont = input()

while cont == "Y":
    print("Please add a name to the list")
    names.append(input())
    print("Would you like to add another name to the list? Y or N")
    cont = input()

print(f"The list has {len(names)} names")

print(
    f"{names[random.randint(0, len(names)-1)]} is going to pay the bill today")
