import sqlite3
from tkinter import *
from tkinter import messagebox as mb
import login_functions
import project_database
import login_DB
back = "#f5ded6"
front = "#672c18"
active_ID = 0


def login():
    name = name_entry.get()
    password = Password_entry.get()
    def role():
        id =pas_w_entry.get()
        result  = login_DB.view1(id)
        if result == None:
            mb.showerror("ERROR MESSAGE", "serial number does not exist" )
        else:
            text_box1.delete(1.0, END)
            text_box1.insert(INSERT, f"hello {result[1]},\n your password is {result[2]}\n your role is {result[3]}")
            global active_ID
            active_ID = id
    if name and password:
        id = name
        id2 = password
        result = login_DB.view_pass(id2)
        result2 = login_DB.view_user(id)
        if result2 == None or result == None:
            mb.showerror("Error", "wrong username or password ")
        else:

            window_3 = Tk()
            window_3.config(bg="white")
            window_3.geometry("1000x600")
            welcome_label = Label(window_3, text=f"welcome {name_entry.get()}", bg="white", fg="black",
                                  font=("segoe ui semibold", 14))
            pas_w_label = Label(window_3, text='Password', bg="white", fg="black", font=("segoe ui semibold", 14))
            pas_w_entry = Entry(window_3, fg="black", highlightcolor="black", highlightthickness=1,
                                font=("segoe ui semibold", 16))
            role_button = Button(window_3, fg=back, bg=front, text="view role", activeforeground=back, activebackground=front,
                                 font=("segoe ui semibold", 14), highlightcolor=front, command=role )
            scrollbar_1 = Scrollbar(window_3)
            text_box1 = Text(window_3, yscrollcommand=scrollbar_1.set, width=33, height=14,
                             font=('segoe ui semibold', 14), highlightbackground="black", highlightthickness=2,
                             highlightcolor="black")


            welcome_label.pack()
            role_button.pack()
            scrollbar_1.pack(side='right', fill=Y)
            text_box1.pack()
            pas_w_label.place(x=10, y=10)
            pas_w_entry.place(x=10,y=70 )
            scrollbar_1.config(command=text_box1.yview)



def createacct():

    def new_acct():

        name = Name_Entry.get()
        password = pword_Entry.get()
        confirm = confirm_pword_Entry.get()
        role = role_Entry.get()
        if name != "" and password != "":
            id = login_DB.getID()
            mb.showinfo("User created", login_DB.data_entry(id, name=Name_Entry.get(), password=pword_Entry.get(), role=role_Entry.get()))
            login_DB.create_table()
        elif name == "admin":
            mb.showerror("Error Message", "username cannot be used")
        elif password != confirm:
            mb.showerror("Error", "password must match")
        elif password == "AdminLogin":
            mb.showerror("Error", "This Password can not be used")
        else:
            mb.showinfo("INFO", "Enter a name and password")
        new_window.destroy()





    new_window = Tk()
    new_window.title("Create account")
    new_window.geometry('1000x600')
    new_window.config(bg="white")

    # Labels
    Name_Label = Label(new_window, text="Enter name", bg='white', fg='black', font=("segoe ui semibold", 14))
    pword_label = Label(new_window, text="Enter password", bg='white', fg='black', font=("segoe ui semibold", 14))
    comfirm_pword_label = Label(new_window, text="comfirm password", bg="white", fg="black", font=("segoe ui semibold", 14))
    role_label = Label(new_window, text="enter Role", bg="white", fg="black", font=("segoe ui semibold", 14))

    # Entries
    Name_Entry = Entry(new_window, fg="black", highlightcolor="black", highlightthickness=1,
                       font=("segoe ui semibold", 16))
    pword_Entry = Entry(new_window, fg="black", highlightcolor="black", highlightthickness=1,
                        font=("segoe ui semibold", 16))
    confirm_pword_Entry = Entry(new_window, fg="black", highlightcolor="black", highlightthickness=1,
                                font=("segoe ui semibold", 16))
    role_Entry = Entry(new_window, fg="black", highlightcolor="black", highlightthickness=1,
                       font=("segoe ui semibold", 16))

    # Buttons
    done_Button = Button(new_window, fg=back, bg=front, text="create", activeforeground=back, activebackground=front,
                         font=("segoe ui semibold", 14), highlightcolor=front, command=new_acct)

    #packing
    Name_Label.pack()
    Name_Entry.pack(pady=10)
    pword_label.pack(pady=10)
    pword_Entry.pack(pady=10)
    comfirm_pword_label.pack(pady=10)
    confirm_pword_Entry.pack(pady=10)
    role_label.pack(pady=10)
    role_Entry.pack(pady=10)

    done_Button.pack(pady=10)



window = Tk()
window.title("Login APP")
window.geometry('1000x600')
window.config(bg=back)

# Labels
title_label = Label(window, text="Enter name and password", bg=back, fg=front, font=('Lucida calligraphy', 16))
name_label = Label(window, text="Name", bg=back, fg=front, font=("segoe ui semibold", 14))
Password_label = Label(window, text="Password", bg=back, fg=front, font=("segoe ui semibold", 14))

# Entries
name_entry = Entry(window, borderwidth=2, highlightcolor=front, highlightthickness=2, font=("segoe ui semibold", 14))
Password_entry = Entry(window, borderwidth=2, highlightcolor=front, highlightthickness=2, font=("segoe ui semibold", 14))

# Buttons
login_button = Button(window, fg=back, bg=front, text="login", highlightcolor=front, activebackground=front,
                      activeforeground=back, font=("segoe ui semibold", 14), command=login)
create_button = Button(window, fg=back, bg=front, text="create account", highlightcolor=front, activebackground=front,
                       activeforeground=back, font=("segoe ui semibold", 14), command=createacct)

# Packing
title_label.pack(expand=True)
name_label.pack(expand=True)
name_entry.pack(expand=True)
Password_label.pack(expand=True)
Password_entry.pack(expand=True)
login_button.pack(expand=True)
create_button.pack(expand=True)

window.mainloop()



