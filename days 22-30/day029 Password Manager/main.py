from tkinter import *
import random
from characters import *
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def pass_generator():
    password = [(alphabet[random.randint(0, len(alphabet)-1)])
                for n in range(1, random.randint(5, 7))]
    for n in range(1, random.randint(2, 4)):
        password.append(numbers[random.randint(0, len(numbers)-1)])
        password.append(symbols[random.randint(0, len(symbols)-1)])
    random.shuffle(password)
    pass_str = "".join(password)
    password_final.delete(0, END)
    password_final.insert(END, string=pass_str)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def pass_save():
    site_name = site_input.get()
    email_name = email_input.get()
    new_pass = password_final.get()
    new_data = {
        site_name: {
            "email": email_name,
            "password": new_pass
        }
    }

    if len(site_name) == 0 or len(new_pass) == 0 or len(email_name) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("password_man.json", "r") as data:
                # reading old data
                pass_data = json.load(data)
        except FileNotFoundError:
            with open("password_man.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            # updating with new data
            pass_data.update(new_data)
            with open("password_man.json", "w") as data:
                # saving uptate data
                json.dump(pass_data, data, indent=4)
        finally:
            email_input.delete(0, END)
            site_input.delete(0, END)
            password_final.delete(0, END)


# ---------------------------- SEARCH SITE ------------------------------- #


def search_site():
    site_name = site_input.get()
    try:
        with open("password_man.json", "r") as data:
            # reading old data
            pass_data = json.load(data)
            site_dict = pass_data[site_name]
    except FileNotFoundError:
        messagebox.showinfo(
            title="Oops", message="There is no recorded passwords!")
    except KeyError as not_found:
        messagebox.showinfo(
            title="Oops", message=f"We found no passwords for {not_found}!")
    else:
        messagebox.showinfo(
            title=site_name, message=f"Email: {site_dict['email']} \nPassword: {site_dict['password']}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
locker_img = PhotoImage(
    file="logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(row=0, column=1)

site_label = Label(text="Site: ", font=(
    "courier", 14), bg="white", padx=10, pady=10, anchor=W)
site_label.grid(row=1, column=0)

site_input = Entry(width=20, font=("courier", 14))
site_input.grid(row=1, column=1)
site_input.get()

search_button = Button(text="Search",
                       command=search_site, width=15)
search_button.grid(row=1, column=2)

email_label = Label(text="E-mail: ", font=(
    "courier", 14), bg="white", padx=10, pady=10)
email_label.grid(row=2, column=0)

email_input = Entry(width=31, font=("courier", 14))
email_input.grid(row=2, column=1, columnspan=2)
email_input.get()

password_label = Label(text="Password: ", font=(
    "courier", 14), bg="white", padx=10, pady=10)
password_label.grid(row=3, column=0)

password_final = Entry(width=20, font=("courier", 14))
password_final.grid(row=3, column=1)

password_button = Button(text="Generate Password",
                         command=pass_generator, width=15)
password_button.grid(row=3, column=2)

password_save = Button(text="Save Password", command=pass_save, width=47)
password_save.grid(row=4, column=1, columnspan=2)


window.mainloop()
