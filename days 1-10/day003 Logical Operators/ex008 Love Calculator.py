print("Welcome to the TRUE LOVE calculator\nCheck if you and your SO are compatible")

print("Type your name:")
name1 = input()
upper_name1 = name1.upper()

print("Type your SO name:")
name2 = input()
upper_name2 = name2.upper()

print(f"Name 1: {upper_name1}\nName 2: {upper_name2}")

love = "LOVE"
true = "TRUE"


def counter(name, key):
    n = 0
    print(name)
    print(key)
    for x in name:
        for y in key:
            if x == y:
                n += 1
    return n


number1 = counter(upper_name1, true)
number2 = counter(upper_name2, true)
number3 = counter(upper_name1, love)
number4 = counter(upper_name2, love)

true_number = number1 + number2
love_number = number3 + number4
score = int(str(true_number) + str(love_number))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
