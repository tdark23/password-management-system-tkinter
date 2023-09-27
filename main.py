from tkinter import *
from tkinter import messagebox
import secrets
import string
import json

RED = "#FE0000"
RETRO = "#7D7463"
GREY = "#A8A196"
BEIGE = "#F4E0B9"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_strong_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3
                and sum(c in string.punctuation for c in password) >= 2):
            return password

def generate_password_and_insert():
    generated_password = generate_strong_password()
    password_entry.delete(0, END)  # Clear the current entry
    password_entry.insert(0, generated_password)  # Insert the generated password


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website_text = website_entry.get()
    email_text = email_entry.get()
    password_text = password_entry.get()
    
    website_length = len(website_text)
    password_length = len(password_text)

    datas_transfered_to_json_file = {
        website_text: {
            "email": email_text,
            "password": password_text
        }
    }

    if website_length == 0 or password_length == 0:
        messagebox.showinfo("Warning", "You can't leave any field empty !")
    else:
        is_ok = messagebox.askokcancel(title=website_text, message=f"These are the details entered \nEmail: {email_text}\nPassword: {password_text}\nIs it ok to save ?")

        if is_ok:
            try:
                with open("datas.json", "r") as file:
                    # reading the datas
                    datas = json.load(file)
            except FileNotFoundError:
                # If the file doesn't exist, create a new JSON file and write the data
                with("datas.js", "w") as file:
                    json.dump(datas_transfered_to_json_file, file, indent=4)
            else:
                datas.update(datas_transfered_to_json_file)
                with open("datas.json", "w") as file:
                    #saving updated datas
                    json.dump(datas_transfered_to_json_file, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50, bg=BEIGE)


# ---------------------------- Labels ------------------------------- #

website = Label(text="Website : ", background=BEIGE)
website.grid(column=0, row=1)

email = Label(text="Email \ Username : ", background=BEIGE)
email.grid(column=0, row=2, padx=10, pady=10)

password = Label(text="Password : ", background=BEIGE)
password.grid(column=0, row=3)

# ---------------------------- Entries ------------------------------- #

website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, padx=10, pady=10)

email_entry = Entry(width=40)
email_entry.insert(0, string="tdark237@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, padx=10, pady=10)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, padx=10, pady=10)


# ---------------------------- Buttons ------------------------------- #

generate_password_button = Button(text="Generate Password", bg=GREY, command=generate_password_and_insert)
generate_password_button.grid(column=2, row=3)

add_password_button = Button(text="Add", width=37, bg=GREY, command=save_password)
add_password_button.grid(column=1, row=4, columnspan=2)

canvas = Canvas(width=200, height=200, background=BEIGE ,highlightthickness=0)
logo = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0,)


window.mainloop()
