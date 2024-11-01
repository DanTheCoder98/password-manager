from tkinter import *
from tkinter import messagebox
import random


def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = []

    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)


def save():
    with open("data.txt", "a") as data_file:
        website = website_input.get()
        email = email_input.get()
        password = password_input.get()

        if len(website) == 0 or len(password) == 0 or len(email) == 0:
            messagebox.showinfo(
                title="Oops",
                message="Please make sure you haven't left any fields empty.",
            )
            return

        is_ok = messagebox.askyesnocancel(
            title=website,
            message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?",
        )

        if not is_ok:
            return

        data_file.write(f"{website} | {email} | {password}\n")

    website_input.delete(0, END)
    email_input.delete(0, END)
    password_input.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=40)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=40)
email_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=22)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

save_button = Button(text="Save", width=37, command=save)
save_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
