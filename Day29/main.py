from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "C", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

    simple_letters= [random.choice(letters) for _ in range(random.randint(0,10))]
    simple_nums=[random.choice(numbers) for _ in range(random.randint(2,4))]
    simple_symbols = [random.choice(symbols) for _ in range(2,4)]
    simple_password = simple_letters+simple_nums+simple_symbols
    random.shuffle(simple_password)
    final_password = "".join(simple_password)

    password.insert(0,final_password)
    pyperclip.copy(final_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_name.get()
    email = user_name.get()
    user_password = password.get()
    new_data = {website:{
            "email":email,
            "password":user_password
        }}
    if len(website) < 5 or len(user_password) < 8:
        messagebox.askretrycancel(title="Invalid entry",message="The entered wesite is not valid OR password lenght is less than 8")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details:\nWebsite: {website}\nEmail/Username: {email}\nPassword: {user_password}\n"
                                    f"Press 'ok' for saving and cancel for edit/exit")
        if is_ok:
            try:
                with open("data.json", "r") as datafile:
                    data=json.load(datafile)
            except FileNotFoundError:
                data={}
            except json.decoder.JSONDecodeError:
                data={}
            data.update(new_data)
            with open("data.json", "w") as datafile:
                json.dump(data, datafile,indent=4)
                pyperclip.copy(user_password)
                website_name.delete(0,END)
                password.delete(0,END)
                website_name.focus()
                
# ---------------------------Find Password ----------------------------#
def find_password():
    website = website_name.get()
    try:
        with open("data.json", "r") as datafile:
            data=json.load(datafile)
    except FileNotFoundError:
        messagebox.showinfo(title="No such data available", message="You are trying to fetch data which is not available.")
    else:
        if website in data:
            email = data[website]["email"]
            user_password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Here is the data:\nEmail: {email}\nPassword: {user_password}")
        else:
            messagebox.showinfo(title="No data Found",message=f"No data for {website}.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas= Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1,sticky="E", pady=2)
user_label = Label(text="Email/Username:")
user_label.grid(column=0,row=2,sticky="E", pady=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3,sticky="E", pady=2)


website_name = Entry(width=21)
website_name.grid(column=1, row=1,sticky="EW", pady=2)
website_name.focus()
user_name = Entry(width=35)
user_name.grid(column=1, row=2,columnspan=2,sticky="EW", pady=2)
user_name.insert(0,"smsawant@gmail.com")
password = Entry(width=21)
password.grid(column=1, row=3,sticky="EW", pady=2)

generate_password = Button(text="Generate Password",command=password_generator)
generate_password.grid(column=2,row=3,sticky="EW", pady=2, padx=5)
searching = Button(text="Search",command=password_generator)
searching.grid(column=2,row=1,sticky="EW", pady=2, padx=5)
add_password = Button(text="Add",width=36,command=save)
add_password.grid(column=1,row=4,columnspan=2,sticky="EW", pady=2)
window.mainloop()