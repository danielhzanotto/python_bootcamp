from tkinter import *
import random
from characters import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


password = []


def add_char(type):
    for _ in range(0, 2):
        get_char = type[random.randint(0, len(type) - 1)]
        pass_index = random.randint(0, len(password) - 1)
        while password[pass_index].isupper() or password[pass_index].isnumeric() or not password[pass_index].isalnum():
            pass_index = random.randint(0, len(password) - 1)
        password[pass_index] = get_char


def pass_generator():
    global password
    if len(password) > 0:
        password = []
    for _ in range(0, 10):
        password.append(alphabet[random.randint(
            0, len(alphabet) - 1)])
    add_char(alphabet_upper)
    add_char(numbers)
    add_char(symbols)
    pass_string = "".join(password)
    password_final.delete(0, END)
    password_final.insert(END, string=f"{pass_string}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def pass_save():
    site_name = site_input.get()
    email_name = email_input.get()
    new_pass = password_final.get()
    if not ".com" in email_name and not "@" in email_name:
        email_label["text"] = "E-mail: Please insert a valid email"
    elif len(site_name) == 0:
        site_label["text"] = "Site: Please insert an input"
    elif len(new_pass) != 10:
        password_label["text"] = "Password: Please insert a valid password"
    else:
        with open("/Users/Daniel/Documents/Phyton Bootcamp/days 22-30/day029 Password Manager/password_man.csv", "a") as f:
            f.write(f"\n{site_name}, {email_name}, {new_pass}")
        email_label["text"] = "E-mail: "
        site_label["text"] = "Site: "
        password_label["text"] = "Password: "


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
locker_img = PhotoImage(
    file="/Users/Daniel/Documents/Phyton Bootcamp/days 22-30/day029 Password Manager/logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(row=0, column=0)

site_label = Label(text="Site: ", font=(
    "courier", 14), bg="white", padx=10, pady=10)
site_label.grid(row=1, column=0)

site_input = Entry(width=30, font=("courier", 14))
site_input.grid(row=2, column=0)
site_input.get()

email_label = Label(text="E-mail: ", font=(
    "courier", 14), bg="white", padx=10, pady=10)
email_label.grid(row=3, column=0)

email_input = Entry(width=30, font=("courier", 14))
email_input.grid(row=4, column=0)
email_input.get()

password_label = Label(text="Password: ", font=(
    "courier", 14), bg="white", padx=10, pady=10)
password_label.grid(row=5, column=0)

password_final = Entry(width=30, font=("courier", 14))
password_final.grid(row=6, column=0)

password_button = Button(text="Generate Password", command=pass_generator)
password_button.grid(row=6, column=1)

password_save = Button(text="Save Password", command=pass_save)
password_save.grid(row=7, column=0)


window.mainloop()
