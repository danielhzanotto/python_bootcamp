from tkinter import *
import pandas
import random
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
BACKGROUND_WHITE = "white"
CARD_COLOR = "#91c2af"

languages = ["French", "English"]
word_french = None

#------Get Words------#


try:
    words_data = pandas.read_csv(
        "/Users/Daniel/Documents/Phyton Bootcamp/days 31-40/day031 Flash Cards/remaining_words.csv")
except FileNotFoundError:
    words_data = pandas.read_csv(
        "/Users/Daniel/Documents/Phyton Bootcamp/days 31-40/day031 Flash Cards/french_words.csv")
    words_data.to_csv(
        "/Users/Daniel/Documents/Phyton Bootcamp/days 31-40/day031 Flash Cards/remaining_words.csv")

words_dict = {}
for index, row in words_data.iterrows():
    words_dict[row.French] = row.English

words_list = [word for word in words_dict]


#------Put Words in card------#


def select_word():
    global word_french
    try:
        word_french = words_list[random.randint(0, len(words_list)-1)]
    except ValueError:
        messagebox.showinfo(
            title="Error", message="It seems that there's no more cards, let's try again!")
        retrieve_words()

    word_english = words_dict[word_french]

    language_label.config(text=languages[0], bg=BACKGROUND_WHITE)
    word_label.config(text=word_french, bg=BACKGROUND_WHITE)
    canvas_card.itemconfig(card, image=card_front)
    window.update()
    window.after(3000, word_translate(word_english))


def word_translate(word):
    language_label.config(text=languages[1], bg=CARD_COLOR)
    word_label.config(text=word, bg=CARD_COLOR)
    canvas_card.itemconfig(card, image=card_back)


#------Take off correct words------#


def word_correct():

    correct_word = [key for key, value in words_dict.items()
                    if value == word_label["text"]]
    correct_word_str = "".join(correct_word)
    words_dict.pop(correct_word_str, None)
    words_list = [word for word in words_dict]
    print(len(words_dict))
    df = pandas.DataFrame(words_dict.items(), columns=languages)
    df.to_csv(
        "/Users/Daniel/Documents/Phyton Bootcamp/days 31-40/day031 Flash Cards/remaining_words.csv")

    select_word()


#------Retrieve Words------#


def retrieve_words():
    global words_dict, words_list

    data = pandas.read_csv(
        "/Users/Daniel/Documents/Phyton Bootcamp/days 31-40/day031 Flash Cards/french_words.csv")
    data.to_csv(
        "/Users/Daniel/Documents/Phyton Bootcamp/days 31-40/day031 Flash Cards/remaining_words.csv")

    words_dict = {}
    for index, row in data.iterrows():
        words_dict[row.French] = row.English

    words_list = [word for word in words_dict]

    select_word()


#------UI------#


window = Tk()
window.title("Flash French Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)


card_front = PhotoImage(
    file="/Users/Daniel/Documents/Phyton Bootcamp/days 31-40/day031 Flash Cards/images/card_front.png")
card_back = PhotoImage(
    file="/Users/Daniel/Documents/Phyton Bootcamp/days 31-40/day031 Flash Cards/images/card_back.png")
right = PhotoImage(
    file="/Users/Daniel/Documents/Phyton Bootcamp/days 31-40/day031 Flash Cards/images/right.png")
wrong = PhotoImage(
    file="/Users/Daniel/Documents/Phyton Bootcamp/days 31-40/day031 Flash Cards/images/wrong.png")


canvas_card = Canvas(height=526, width=800,
                     bg=BACKGROUND_COLOR, highlightthickness=0)
card = canvas_card.create_image(400, 263, image=card_front)
canvas_card.grid(row=0, column=0, rowspan=5, columnspan=3)


language_label = Label(text="", font=(
    "Arial", 20, "italic"), bg=BACKGROUND_WHITE)
language_label.grid(row=1, column=1)

word_label = Label(text="", font=(
    "Arial", 50, "bold"), bg=BACKGROUND_WHITE)
word_label.grid(row=2, column=1)

button_wrong = Button(image=wrong, command=select_word, borderwidth=0)
button_wrong.grid(row=5, column=2)

button_right = Button(image=right, command=word_correct, borderwidth=0)
button_right.grid(row=5, column=0)

button_start = Button(text="Retrieve All Cards", font=(
    "Arial", 14, "italic"), bg=BACKGROUND_COLOR, command=retrieve_words, borderwidth=0)
button_start.grid(row=5, column=1)

select_word()

window.mainloop()
