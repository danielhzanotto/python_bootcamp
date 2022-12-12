from tkinter import *

window = Tk()


def button_clicked():
    my_label["text"] = input.get()


# how to create a window
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# how to create a label
my_label = Label(text="I Am a Label", font=("Courier", 18))
my_label.grid(column=0, row=0)
my_label["text"] = "New Text"

# how to create a button
button = Button(text="Click Me", command=button_clicked)
button.grid(row=1, column=1)

# how to create an entry input
input = Entry(width=30)
input.grid(row=2, column=3)
input.insert(END, string="Some text to begin with")
input.get()


new_button = Button(text="New Button", command=button_clicked)
new_button.grid(row=0, column=2)


window.mainloop()
