print("Please insert a word")
word = input()

hidden_word_list = []

for l in word:
    hidden_word_list.append("_")
print(" ".join(hidden_word_list))

print("Type a letter")
letter = input()


letter_index = 0
hang_fill = 0
for l in word:
    if letter == l:
        hidden_word_list[letter_index] = letter
    letter_index += 1


print(" ".join(hidden_word_list))
