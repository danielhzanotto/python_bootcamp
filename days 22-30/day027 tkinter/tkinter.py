import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I Am a Label", font=("Courier", 18))
my_label.pack(side="left")


my_label["text"] = "New Text"














window.mainloop()
