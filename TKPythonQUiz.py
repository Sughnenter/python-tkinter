#Python program for a simple quiz app
from tkinter import  *
from tkinter import messagebox as mb
import ttkbootstrap
def allocate():
    Q1 = Q1Entry.get()
    if Q1 != " ":
        if mb.askyesno("confirmation","Is this your final answer"):
            answer = ('Jupiter')
        else:
            mb.showwarning("Note","Enter another answer and try again")
    else:
        mb.showerror("Input error", "Error: You have to answer first")
    output = "Jupiter"
    result.config(text=output)
    mb.showinfo("Success message",output)
def questiontwo():
    Q2 =Q2Entry.get()
    if Q2 != " ":
        if mb.askyesno("confirmation","Is this your final answer"):
            a1 = ('Venus')
        else:
            mb.showwarning("Note","Enter another answer and try again")
    else:
        mb.showerror("Input error", "Error: You have to answer first")
    output = "Venus"
    result.config(text=output)
    mb.showinfo("Sucess message",output)
def questionthree():
    Q3 =Q3Entry.get()
    if Q3 != " ":
        if mb.askyesno("confirmation","Is this your final answer"):
            answer3 = ('Uranus')
        else:
            mb.showwarning("Note","Enter another answer and try again")
    else:
        mb.showerror("Input error", "Error: You have to answer first")
    output = "Uranus"
    result.config(text=output)
    mb.showinfo("Sucess message",output)
def questiinfour():
    Q4 =Q4Entry.get()
    if Q4 != " ":
        if mb.askyesno("confirmation","Is this your final answer"):
            answer4 = ('Mercury')
        else:
            mb.showwarning("Note","Enter another answer and try again")
    else:
        mb.showerror("Input error", "Error: You have to answer first")
    output = "Mercury"
    result.config(text=output)
    mb.showinfo("Sucess message",output)
def questionfive():
    Q5 =Q5Entry.get()
    if Q5 != " ":
        if mb.askyesno("confirmation","Is this your final answer?"):
            answer5 = ('Neptune')
        else:
            mb.showwarning("Note","Enter another answer and try again")
    else:
        mb.showerror("Input error","Error: You have to answer first")
    op =f"OUTPUT\nthe correct answer is Neptune"
    result.config(text=op)
    mb.showinfo("Success message",op)
window = Tk()
window.title("Allocator App")
window.geometry("850x650")
window.config(bg="green")
myText = Label(window, text="PLANETARY QUIZ", fg="white", bg="green", font=("Verdana"))
Q1label = Label(window, text="question one(1):what planet is the biggest?", fg="white", bg="green", font=("Verdana"))
Q2label = Label(window, text="Question Two(2):what planet is the hottest?", fg="white", bg="green", font=("Verdana"))
Q3label = Label(window, text="Question three(3):what planet is the coldest?", fg="white", bg="green", font=("Verdana"))
Q4label = Label(window, text="Question Four(4):what planet is closest to the sun?", fg="white", bg="green", font=("Verdana"))
Q5label = Label(window, text="Question Five(5)what planet is Farthest from the sun?", fg="white", bg="green", font=("Verdana"))
result = Label(window, text = 'answer',fg='white',bg='green',font=("Verdana",22))
# ENTRIES
Q1Entry = Entry(window, font=("Verdana", 18), width=20)
Q2Entry = Entry(window, font=("verdana", 18), width=20)
Q3Entry = Entry(window, font=("verdana", 18), width=20)
Q4Entry = Entry(window, font=("verdana", 18), width=20)
Q5Entry = Entry(window, font=("verdana", 18), width=20)
# BUTTONS
q1= Button(window, text="CONFIRM", font=("Tahoma", 18), command=allocate)
q2= Button(window,text="CONFIRM",font=("Tahoma",18),command=questiontwo)
q3= Button(window,text="CONFIRM",font=("Tahoma",18),command=questionthree)
q4= Button(window,text="CONFIRM",font=("Tahoma",18),command=questiinfour)
q5= Button(window,text="CONFIRM",font=("Tahoma",18),command=questionfive)
myText.place(x=15,y=10)
Q1label.place(x=15,y=55)
Q1Entry.place(x=470,y=55)
Q2label.place(x=15,y=155)
Q2Entry.place(x=470,y=155)
Q3label.place(x=15,y=255)
Q3Entry.place(x=470,y=255)
Q4label.place(x=15,y=355)
Q4Entry.place(x=470,y=355)
Q5label.place(x=15,y=455)
Q5Entry.place(x=470,y=455)
result.place(x=400,y=555)
q1.place(x=470,y=93)
q2.place(x=470,y=193)
q3.place(x=470,y=293)
q4.place(x=470,y=393)
q5.place(x=470,y=493)
window.mainloop()