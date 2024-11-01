from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt", "a") as data_file:
        data_file.write(
            f"{website_input.get()} | {email_input.get()} | {password_input.get()}\n"
        )

    website_input.delete(0, END)
    email_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
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

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

save_button = Button(text="Save", width=37, command=save)
save_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
