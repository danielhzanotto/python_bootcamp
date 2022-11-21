import random

number = random.randint(1, 2)
toss_coin = ""

if number == 1:
    toss_coin = "Heads"
else:
    toss_coin = "Tails"

print(toss_coin)
