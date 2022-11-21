import random

print("Welcome to BlackJack Python!!")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

pc_total = 0
your_total = 0
cont = ""


def get_card(): return cards[random.randint(0, len(cards) - 1)]


def counting_cards(cards):
    total = 0
    for card in cards:
        total += card
    return total


def final_counter(you, pc):
    print()
    print(f"Your cards are: {your_cards}: {you}")
    print(f"The PC card is: {pc_cards}: {pc}")

    if you < pc or you > 21:
        print("You lost!")
    elif pc < you:
        print("You won!")
    else:
        print("It's a match")


def over_21(cards):
    for i in cards:
        if i == 11:
            cards.remove(11)
            cards.append(1)


your_cards = []
for n in range(0, 2):
    your_cards.append(get_card())

pc_cards = [get_card()]

print(f"Your cards are: {your_cards}")
print(f"The PC card is: {pc_cards}")


print("Type 'y' to get another card, type 'n' to pass:")
cont = input().lower()

while cont == "y":

    your_cards.append(get_card())
    your_total = counting_cards(your_cards)
    if your_total > 21:
        over_21(your_cards)

    print(f"Your cards are: {your_cards}")
    your_total = counting_cards(your_cards)

    if your_total > 21:
        cont = "n"
        print("You passed 21")
    else:
        print("Type 'y' to get another card, type 'n' to pass:")
        cont = input().lower()

if cont == "n":
    your_total = counting_cards(your_cards)
    while pc_total < 21:
        pc_cards.append(get_card())
        pc_total = counting_cards(pc_cards)

        if pc_total > 21:
            over_21(pc_cards)

        pc_total = counting_cards(pc_cards)
        if pc_total > 21:
            pc_cards.pop()
            pc_total = counting_cards(pc_cards)
            break

final_counter(your_total, pc_total)
