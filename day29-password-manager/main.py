from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    pw_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    nr_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    nr_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = nr_letters + nr_symbols + nr_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pw_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # pw_keys = ["Website:", "Email/Username:", "Password:"]
    # pw_values = [website_entry.get(), email_un_entry.get(), pw_entry.get()]
    # pw_dict = {key:value for (key, value) in zip(pw_keys, pw_values)}
    # file_data = " | ".join(f"{key} {value}" for key, value in zip(pw_keys, pw_values)) + "\n"
    website = website_entry.get().title()
    email = email_un_entry.get()
    password = pw_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not all([website, email, password]):
        messagebox.showinfo(title="Oops", message="Please don't leave any empty fields!")
    # else:
    #     is_ok = messagebox.askokcancel(title="", message=f"These are the details entered: \nWebsite: {website} "
    #                                                      f"\nEmail: {email}  \nPassword: {password} \nIs it ok to save?")
    else:
        try:
            with open("Passwords.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("Passwords.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("Passwords.json", mode="w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pw_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    search_query = website_entry.get().title()
    try:
        with open("passwords.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="", message="No Data File Found!")
    else:
        if search_query in data:
            messagebox.showinfo(title="", message=f"Access for {search_query}: "
                                                  f"\nEmail: {data[search_query]['email']}"
                                                  f"\nPassword: {data[search_query]['password']}")
        else:
            messagebox.showinfo(title="", message=f'No details for "{search_query}" exists')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Shiro's Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_un_label = Label(text="Email/Username:")
email_un_label.grid(column=0, row=2)
pw_label = Label(text="Password:")
pw_label.grid(column=0, row=3)

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="NSEW")
website_entry.focus()
email_un_entry = Entry()
email_un_entry.grid(column=1, row=2, columnspan=2, sticky="NSEW")
email_un_entry.insert(0, "maruchan31@gmail.com")
pw_entry = Entry()
pw_entry.grid(column=1, row=3, sticky="NSEW")

# Buttons
search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="NSEW")
gen_pw_button = Button(text="Generate Password", command=generate_password)
gen_pw_button.grid(column=2, row=3)
add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="NSEW")

window.mainloop()
