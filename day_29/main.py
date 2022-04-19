from tkinter import *
from  tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
symbol = ["!","£","$","%","^","&","*","-","(",")","+"]
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
is_upper_lower = 0
number = [0,1,2,3,4,5,6,7,8,9]

def generate_password():
    new_pass = ""
    for _ in range(0,20):
        ran_num = random.randint(0,2)
        if ran_num==0:
            new_pass+=random.choice(symbol)
        elif ran_num==1:
            letter = random.choice(letters)
            is_upper_lower = random.randint(0,1)
            if is_upper_lower==0:
                new_pass+=str(letter).upper()
            else:
                new_pass+=str(letter).lower()
        else:
            new_pass+=str(random.choice(number))

    password_entry.insert(index=0,string=new_pass)
    window.clipboard_clear()
    window.clipboard_append(string=new_pass)
def save():
    if website_entry.get() == "":
        messagebox.showwarning(message="Please fill in the webste")
        return
    if email_entry.get() == "":
        messagebox.showwarning(message="Please fill in the email")
        return
    if password_entry.get() == "":
        messagebox.showwarning(message="Please fill in your password")
        return
    with open("password.txt",mode="a") as password_reader:
        password_reader.write(f"{website_entry.get()} | ")
        password_reader.write(f"{email_entry.get()} | ")
        password_reader.write(f"{password_entry.get()}\n")
    messagebox.showinfo(message="Password save successfully")
    window.destroy()


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#create window to display component.
window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=40)
#create component
canvas = Canvas(height=200,width=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock)
web_label = Label(text="Website:")
email_username_label = Label(text="Email/Username")
password_label = Label(text="Password:")
generate_password_button = Button(text="Generate Password")
generate_password_button.config(width=15)
add_button =Button(text="Add",width=36)
website_entry = Entry(width=35)
email_entry = Entry(width=35)
password_entry = Entry(width=21)

#layout
canvas.grid(row=0,column=1,sticky="EW")
web_label.grid(row=1,column=0,sticky="EW")
website_entry.grid(row=1,column=1,columnspan=2,sticky="EW")
email_username_label.grid(row=2,column=0,sticky="EW")
email_entry.grid(row=2,column=1,columnspan=2,sticky="EW")
password_label.grid(row=3,column=0,sticky="EW")
password_entry.grid(row=3,column=1,sticky="EW")
generate_password_button.grid(row=3,column=2,sticky="EW")
generate_password_button.config(command=generate_password)
add_button.grid(row=4,column=1,columnspan=2,sticky="EW")
add_button.config(command=save)
window.mainloop()
