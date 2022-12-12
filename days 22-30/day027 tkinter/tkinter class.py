import tkinter

window = tkinter.Tk()

# how to create a window
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# how to create a label
my_label = tkinter.Label(text="I Am a Label", font=("Courier", 18))
my_label.pack()
my_label["text"] = "New Text"


# button functionality
def button_clicked():
    my_label["text"] = input.get()


# how to create a button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# how to create an entry input
input = tkinter.Entry(width=10)
input.pack()
input.get()


window.mainloop()
