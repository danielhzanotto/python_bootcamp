import random
import art
import game_data
# from replit import clear


print(art.logo)

compare_a = {}
compare_b = {}


def get_random(): return game_data.data[random.randint(
    0, len(game_data.data) - 1)]


def not_equal(a, b):
    b = get_random()
    if a["name"] == b["name"]:
        b = get_random()
    return b


compare_a = get_random()
compare_b = not_equal(compare_a, compare_b)


# print(compare_a["follower_count"], compare_b["follower_count"])
keep_playing = True
keep_record = 0
correct = True
score = 0
guess = ""
while keep_playing:
    while correct:

        print("Compare A:", compare_a["name"], ", a",
              compare_a["description"], "from", compare_a["country"])
        print(art.vs)
        print("Against B:", compare_b["name"], ", a",
              compare_b["description"], "from", compare_b["country"])

        answer = compare_a["follower_count"] > compare_b["follower_count"]
        guess = input().lower()
        if guess == 'a' and answer:
            print("Correct!")
            score += 1
            compare_b = not_equal(compare_a, compare_b)

        elif guess == 'b' and not answer:
            print("Correct!")
            score += 1
            compare_a = compare_b
            compare_b = not_equal(compare_a, compare_b)

        elif (guess == 'a' and not answer) or (guess == 'b' and answer):
            print(f"Sorry, that's wrong! Your score is {score}")
            correct = False
        else:
            print("Type a correct input")

    if keep_record <= score:
        keep_record = score
    print(f"Your best score so far is {keep_record}")

    print("Do you want to keep playing? y / n")
    keep = input().lower()
    if keep == "y":
        correct = True
        score = 0
        compare_a = get_random()
        compare_b = not_equal(compare_a, compare_b)
    else:
        keep_playing = False
