import positions  # pieces of the hangman from another file
import hangman_words  # import words to the game
import random

# write the word
print(positions.logo)

word = hangman_words.word_list[random.randint(
    0, len(hangman_words.word_list) - 1)]


# print a series of "_" with the number of letters of the word
hidden_word_list = []  # here will be the "_"
for l in word:
    hidden_word_list.append("_")
print(" ".join(hidden_word_list))


wrong_guesses = []

# THE GAME
completed_game = False
hangman_counter = len(positions.hangman) - 1
# while the hangman is't complete and all the letters aren't guessed, the game is on, if one of these change, the game ends
while hangman_counter > 0 and completed_game == False:

    # type a letter
    print("Type a letter")
    letter = input()

# if letter is in word, substitute _ by letter at position
    letter_index = 0  # position of the letter on word
    hang_fill = 0  # if this number is 0 by the end of the round, so loses one life
    if len(letter) == 1 and letter.isalpha():
        for l in word:
            if letter == l:
                # if letter is equal to the word's letter in "letter_index" position, so the hidden word gets the letter
                hidden_word_list[letter_index] = letter
                hang_fill += 1
                print(positions.hangman[hangman_counter])

    # if the word is complete, you won
            # if the list hidden word is a complete word, the game ends
            if "".join(hidden_word_list).isalpha() == True:
                completed_game = True

            letter_index += 1  # every time the loop ends, the position to be filled increases

    # if not, insert a part of the hangman
        if hang_fill == 0:  # if the given letter found no matches at the word, this counter keeps 0 and the player loses a life
            hangman_counter -= 1
            print(positions.hangman[hangman_counter])
            wrong_guesses.append(letter)
            print(" ".join(wrong_guesses))
    else:
        print("Type again")

# print word
    print(" ".join(hidden_word_list))

# final result
if hangman_counter == 0:
    print("you lost")
    print(f"the word was {word}")
else:
    print("you won")
