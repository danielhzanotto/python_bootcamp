import random

animals = ["arkvard", "baboon", "lion", "llama", "bison", "bear", "koala"]

random_animal = animals[random.randint(0, len(animals) - 1)]

print(random_animal)

print("please type a letter")
letter = input().lower()

for l in random_animal:
    print(l == letter)
