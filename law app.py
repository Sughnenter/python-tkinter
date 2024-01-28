from tkinter import *
import tkinter as tk
import sqlite3
import law_firm_db
from tkinter import messagebox as mb
def LOG_PAGE():
    # Function to handle registration
    def LOG():
        # Retrieve user inputs
        username = username_entry.get()
        password = password_entry.get()

        # Connect to the database
        conn = sqlite3.connect("law_firm.db")
        cursor = conn.cursor()

        # Create a table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        """)

        # Insert new member into the database
        cursor.execute("INSERT INTO members (username, password) VALUES (?, ?)", (username, password))
        conn.commit()

        # Close the database connection
        conn.close()

        # Display registration success message
        mb.showinfo("LOGIN", "Login Successful!")

    app =Tk()
    app.geometry("600x400")
    app.title("Law Firm App")
    app.config(bg="black")

    # Header
    header_frame = tk.Frame(app, bg="gold", height=70, width=599).place(x=0, y=0)
    header_label = tk.Label(header_frame, text="LAW FIRM APP", fg="white", bg="gold",
                            font=("Antique Olive Compact", 15))
    header_label.place(x=240, y=30)

    # Welcome Label
    welcome_label = tk.Label(app, text="Welcome", fg="white", bg="black", font=("Antique Olive Compact", 15))
    welcome_label.place(x=230, y=90)

    # Login Frame
    LOG_frame = tk.Frame(app, bg="black")
    LOG_frame.place(x=200, y=150)

    username_label = tk.Label(LOG_frame, text="Username:", fg="white", bg="black")
    username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    username_entry = tk.Entry(LOG_frame)
    username_entry.grid(row=0, column=1, padx=5, pady=5)

    password_label = tk.Label(LOG_frame, text="Password:", fg="white", bg="black")
    password_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    password_entry = tk.Entry(LOG_frame, show="*")
    password_entry.grid(row=1, column=1, padx=5, pady=5)

    LOG_button = tk.Button(app, fg="black", bg="white", text="LOGIN", font=("Antique Olive Compact", 15),command=LOG)
    LOG_button.place(x=230, y=240)
def REG_PAGE():

    def REG():
        # Retrieve user inputs
        username = name_entry.get()
        password = password_entry.get()
        def register_user():
            name = name_entry.get()
            password = password_entry.get()
            if name != "" and password!="":
                mb.showinfo("data entered", law_firm_db.user_entry(name, password))
        

    window_1 = Tk()
    window_1.geometry("600x400")
    window_1.title ("Register")
    window_1.config(bg="black")
    #b37f10
    #LABELS
    name_label = Label(window_1, text="username", bg="black", fg="#b37f10", font=('tahoma', 17))
    password_label = Label(window_1, text="password", bg="black", fg="#b37f10", font=('tahoma', 17))
    #ENTRIES
    name_entry = Entry(window_1, font=('tahoma', 17))
    password_entry = Entry(window_1, font=('tahoma', 17))
    #BUTTON
    confirm_button = Button(window_1, text="Confirm", font=('tahoma', 14),command= REG())
    name_label.pack(expand=True)
    name_entry.pack(expand=True)
    password_label.pack(expand=True)
    password_entry.pack(expand=True)
    confirm_button.pack(expand=True) 

   

app = Tk()
app.geometry("600x400")
app.title("LAW")
app.config(bg="black")

# def LoginPage():

cavn_1 = Frame(app, bg="gold", height=70, width=599).pack()
header = Label(app, text="LAW APP", fg="white", bg="gold", font=("Antique Olive Compact", 15)).place(x=240, y=30)
WELCOME = Label(app, text="WELCOME", fg="white", bg="black", font=("Antique Olive Compact", 15)).place(x=230, y=90)
OR_ = Label(app, text="OR", fg="white", bg="black", font=("Antique Olive Compact", 9)).place(x=299, y=350)
# BUTTONS

# Buttons in the middle
button1 = Button(app, fg="black", bg="white", text="LAWS", font=("Antique Olive Compact", 10))
button1.place(x=230,y=150)
button2 = Button(app, fg="black", bg="white", text="DICTIONARY", font=("Antique Olive Compact", 10))
button2.place(x=330,y=150)
button3 = Button(app, fg="black", bg="white", text="DECIDED CASES", font=("Antique Olive Compact", 10))
button3.place(x=230,y=220)
# button4 = Button(app, fg="black", bg="white", text="Button 4", font=("Antique Olive Compact", 10))
# button4.place(x=330,y=220)
login_bttn = Button(app, fg="black", bg="white", text="LOGIN", font=("Antique Olive Compact", 10),command=LOG_PAGE).place(x=230,y=350)
register_bttn = Button(app, fg="black", bg="white", text="REGISTER", font=("Antique Olive Compact", 10),command=REG_PAGE).place(x=330, y=350)

app.resizable(False, False)
app.mainloop()