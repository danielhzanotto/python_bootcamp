from tkinter import *

window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)


def button_clicked():
    label_km_value["text"] = int(input.get()) * 1.609


input = Entry(width=7)
input.get()

label_miles = Label(text="Miles", font=("Courier", 12))
label_is_equal = Label(text="Is equal to", font=("Courier", 12))
label_km_value = Label(text="0", font=("Courier", 12))
label_km = Label(text="Kilometers", font=("Courier", 12))
button = Button(text="Calculate", command=button_clicked)

input.grid(row=0, column=1)
label_miles.grid(row=0, column=2)
label_is_equal.grid(row=1, column=0)
label_km_value.grid(row=1, column=1)
label_km.grid(row=1, column=2)
button.grid(row=2, column=1)

window.mainloop()
