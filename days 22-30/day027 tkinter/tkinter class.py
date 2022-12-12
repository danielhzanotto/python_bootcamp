from tkinter import *

window = Tk()


# functions
def button_clicked():
    my_label["text"] = input.get()


def spinbox_used():
    print(spinbox.get())


def checkbutton_used():
    print(checked_state.get())


def radio_used():
    print(radio_state.get())


def scale_used(value):
    print(value)


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


# how to create a window
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# how to create a label
my_label = Label(text="I Am a Label", font=("Courier", 18))
my_label.pack()
my_label["text"] = "New Text"

# how to create a button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# how to create an entry input
input = Entry(width=30)
input.pack()
input.insert(END, string="Some text to begin with")
input.get()

# hot to create text
text = Text(height=5, width=30)
text.focus()  # put cursor in textbox
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))  # get caracter 0 from line 1
text.pack()

# how to create a spinbox
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# how to create a scale
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# how to create a checkbox
checked_state = IntVar()
checkbutton = Checkbutton(
    text="Is On?", variable=checked_state, command=checkbutton_used)

# how to create radio button
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1,
                           variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2,
                           variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(text="Option 3", value=3,
                           variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

# how to create a listbox
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
