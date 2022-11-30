import random
import logo

print(logo.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

number_guess = random.randint(1, 100)
difficulty_points = 0
guess = 0


print("Choose a difficulty. Type 'easy' or 'hard'")
difficulty = input().lower()
while not difficulty == "easy" and not difficulty == "hard":
    print("Please type a valid input. Type 'easy' or 'hard'")
    difficulty = input().lower()

if difficulty == "easy":
    difficulty_points = 10
elif difficulty == "hard":
    difficulty_points = 5

print(f"You have {difficulty_points} attempts remaining.")
print("Make a guess")

while difficulty_points > 0:
    guess = int(input())
    print(guess)
    if guess == number_guess:
        break
    elif guess > number_guess:
        print("Too high")
        difficulty_points -= 1
    elif guess < number_guess:
        print("Too low")
        difficulty_points -= 1
    if difficulty_points > 0:
        print(f"You have {difficulty_points} attempts remaining.")
        print("Guess Again")

if difficulty_points > 0:
    print(
        f"You got it! Your guess was {guess} and the answer is {number_guess}")
elif difficulty_points == 0:
    print(
        f"You ran out of attempts, you lost. The correct answer was {number_guess}")
