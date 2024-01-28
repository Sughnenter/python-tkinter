import sqlite3
from tkinter import *
from tkinter import messagebox as mb
import DBfunctions
import Db
active_ID = 0
def clear():
    serial_Entry.delete(0, END)
    name_Entry.delete(0, END)
    gender_Entry.delete(0, END)
    Role_Entry.delete(0, END)
    Password_Entry.delete(0, END)
    global active_ID
    active_ID = 0


def admin_login():
    name = name_Entry.get()
    password = Password_Entry.get()
    role = Role_Entry.get()
    if role == "admin".upper() or role == "ADMIN".lower() and name =="Shammah Johnson" and password == "AdminLogin":
        mb.showinfo("WELCOME MESSAGE", f"Welcome {name}, your role is {role},you can view and update database")
        viewDB()
    else:
        mb.showerror("ERROR MESSAGE", "Password is incorrect")
def viewDB():
    if Password_Entry.get() == "AdminLogin":
        data = DBfunctions.view()
        text_box1.delete(1.0, END)
        text_box1.insert(INSERT, F"S/N \t | NAME \t   |GENDER \t |ROLE \t |\n")
        for i in data:
            text_box1.insert(INSERT, f"{i[0]} | {i[1]}  \t\t |{i[2]}\t |{i[3]}|\n")
    else:
        mb.showerror("ERROR MESSAGE", "WRONG PASSWORD")


def add_student():
    if Password_Entry.get() == "AdminLogin":
        serial = serial_Entry.get()
        name = name_Entry.get()
        gender = gender_Entry.get()
        role = Role_Entry.get()
        if name != "" and role != "":
            id = DBfunctions.getID()
            mb.showinfo('Data entered', DBfunctions.data_entry(id, name, gender, role))
        DBfunctions.create_table()
        view_text()
    else:
        mb.showerror("ERROR MESSAGE", "wrong password")


def view_text():
    data = DBfunctions.view()
    text_box1.delete(1.0, END)
    text_box1.insert(INSERT, f" S/N | Name \t\t | Gender | Role\t|\n")
    for i in data:
        text_box1.insert(INSERT, f"{i[0]}| {i[1]} \t\t | {i[2]}|{i[3]}\t|\n")


def view_status():
    id = serial_Entry.get()
    result = DBfunctions.view1(id)
    if result == None:
        mb.showerror("ERROR MESSAGE", "Serial Number does not exist")
    else:
        text_box1.delete(1.0, END)
        text_box1.insert(INSERT, F"Your name is {result[1]},\n Gender is {result[2]},\n Role is {result[3]}")
    global active_ID
    active_ID = id

def update():
    if int(active_ID) > 0:
        mb.showinfo("Success Message", DBfunctions.update(active_ID, name_Entry.get(), gender_Entry.get(), Role_Entry.get()))
        viewDB()
        clear()
    else:
        mb.showerror("Error Message", "error: serial number is invalid")

def delete():
    if int(active_ID) > 0:
        mb.showinfo("Success Message", DBfunctions.delete(active_ID))
        viewDB()
        clear()
    else:
        mb.showerror("ERROR MESSAGE", "ERROR: Select a valid serial number")

back = "#f5ded6"
front = "#672c18"
window = Tk()
window.title("Database")
window.geometry('1000x600')
window.config(bg=back)



# Frames
left_frame = Frame(window, bg=back, height=580, width=400, highlightbackground=back, highlightthickness=2, highlightcolor=front)
middle_frame = Frame(window, bg="white", height=580, width=2)
right_frame = Frame(window, bg=back, height=580, width=550, highlightbackground=back, highlightthickness=2,highlightcolor=front)
# Labels
title_label = Label(left_frame, text="USER LOGIN", bg=back, fg=front, font=('Helvetica bold', 20))
serial_label = Label(left_frame, text=" Enter S/N:", bg=back, fg=front, font=('Helvetica bold', 17), borderwidth=1, relief="solid", height=1)
name_label = Label(left_frame, text="NAME:", bg=back, fg=front, font=('Helvetica bold', 14))
gender_label = Label(left_frame, text="GENDER:", bg=back, fg=front, font=('Helvetica bold', 14))
Role_label = Label(left_frame, text="ROLE", bg=back, fg=front, font=('Helvetica bold', 14))
Password_label = Label(left_frame, text="PASSWORD", bg=back, fg=front, font=('Helvetica bold', 14),borderwidth=1, relief="solid", height=1)
registered_label = Label(right_frame, text="CURRENT USER", bg=back, fg=front, font=('Helvetica bold', 20))
# ENTRIES
serial_Entry = Entry(left_frame, bg=back, fg=front, font=("Helvetica bold", 19), width=4)
name_Entry = Entry(left_frame, bg=back, fg=front, font=("Helvetica bold", 14))
gender_Entry = Entry(left_frame, bg=back, fg=front, font=("Helvetica bold", 14))
Role_Entry = Entry(left_frame, bg=back, fg=front, font=("Helvetica bold", 14))
Password_Entry = Entry(left_frame, bg=back, fg=front, font=("Helvetica bold", 14), show="*")
# scrollbars
scrollbar_1 = Scrollbar(right_frame)
# text box
text_box1 = Text(right_frame, yscrollcommand=scrollbar_1.set, width=42, height=13, font=('helvetica bold', 14))

# BUTTONS
clear_Button = Button(left_frame, bg=front, fg=back, activebackground=front, activeforeground=back, text="Clear",
                      font=('Helvetica bold', 14), command=clear)
submit_Button = Button(left_frame, bg=front, fg=back, activebackground=front, activeforeground=back, text="Submit",
                       font=('Helvetica bold', 14), command=add_student)
select_Button = Button(left_frame, bg=front, fg=back, activebackground=front, activeforeground=back, text="Select",
                       font=('Helvetica bold', 14))#, command=single_student)
delete_Button = Button(left_frame, bg=front, fg=back, activebackground=front, activeforeground=back, text="delete",
                       font=('Helvetica bold', 14), command=delete)
update_Button = Button(left_frame, bg=front, fg=back, activebackground=front, activeforeground=back, text="update",
                       font=('Helvetica bold', 14), command=update)
login_Button = Button(left_frame, bg=front, fg=back, activebackground=front, activeforeground=back,  text='login',
                     font=('Helvetica bold', 14), command=view_status)

view_Button = Button(right_frame, bg=front, fg=back, activebackground=front, activeforeground=back,  text='view',
                     font=('Helvetica bold', 14),command=viewDB)
admin_Button = Button(right_frame, bg=front, fg=back, activebackground=front, activeforeground=back,  text='Admin Login',
                     font=('Helvetica bold', 14), command=admin_login)

# Frame Propagation
left_frame.propagate(0)
middle_frame.propagate(0)
right_frame.propagate(0)
# Frame packing
left_frame.place(x=20, y=10)
middle_frame.place(x=420, y=10)
right_frame.place(x=425, y=10)
# Placements
title_label.place(x=130, y=15)
name_label.place(x=15, y=70)
name_Entry.place(x=130, y=70)
gender_label.place(x=15, y=110)
gender_Entry.place(x=130, y=110)
Role_label.place(x=15, y=150)
Role_Entry.place(x=130, y=150)
clear_Button.place(x=145, y=230)
submit_Button.place(x=215, y=230)
Password_label.place(x=15, y=370)
Password_Entry.place(x=145, y=370)
serial_label.place(x=15, y=310)
serial_Entry.place(x=130, y=310)
login_Button.place(x=165, y=420)
delete_Button.place(x=165, y=500)
update_Button.place(x=255, y=500)
select_Button.place(x=75, y=500)
registered_label.place(x=140, y=10)
scrollbar_1.pack(side="right", fill=Y)
text_box1.place(x=27, y=70)
scrollbar_1.config(command=text_box1.yview)
view_Button.place(y=384, x=170)
admin_Button.place(y=384, x=260)


window.mainloop()
