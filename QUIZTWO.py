#Create a simple quiz with radio buttons atleast five questions the quiz should print a result a remark
#the quiz should have at least give questions each carrying ten marks it should display total correct answers
#
from tkinter import *
from tkinter import messagebox as mb
import ttkbootstrap as ttk


def submit():
    name = nameentry.get()
    number = numberEntery.get()
    a1 = ""
    if q1.get() == 1:
        a1 = "Jupiter"
        mb.showinfo("SCORE", "10 marks")
    elif q1.get() == 2:
        a1 = "Neptune"
        mb.showinfo("SCORE", "You failed this question")
    else:
        a1 = "Not selected"
    a2 = ""
    if q2.get() == 1:
        a2 = "Mercury"
        mb.showinfo("SCORE", "You failed this question")
    elif q2.get() == 2:
        a2 = "Venus"
        mb.showinfo("SCORE", "10 marks")
    else:
        a2 = "Not selected"
    a3 = ""
    if q3.get() == 1:
        Q3 = "Uranus"
        mb.showinfo("SCORE", "10 marks")
    elif q3.get() == 2:
        Q3 = "Neptune"
        mb.showinfo("SCORE", "You failed this question")
    else:
        Q3 = "Not selected"
    Q4 = ""
    if q4.get() == 1:
        Q4 = "Mercury"
        mb.showinfo("SCORE", "10 marks")
    elif q4.get() == 2:
        Q4 = "Earth"
        mb.showinfo("SCORE", "You failed this question")
    else:
        Q4 = "Not selected"
    Q5 = ""
    if q5.get() == 1:
        Q5 = "Mars"
        mb.showinfo("SCORE", "You failed this question")
    elif q5.get() == 2:
        Q5 = "Neptune"
        mb.showinfo("SCORE", "10 marks")
    else:
        Q5 = "Not selected"
    #total=q1+q2+q3+q4+q5
    info = f"name is {name}\n admission number is {number}"
    mb.showinfo("DETAILS",info)
    mb.showinfo("REMARK", "You did great")
back="#7bc05c"
fore="black"
body=Tk()
body.title("Quiz App")
body.geometry("1150x600")
body.config(bg=back)
heading=Label(body,text="QUIZ APPLICATION",bg=back,fg=fore,font=("David",40))
namelabel=Label(body,text="Enter your full name:",bg=back,fg=fore,font=("David",18))
numberLabel=Label(body,text="Enter your Admission Number:",bg=back,fg=fore,font=("David",18))
question=Label(body,text="Answer the following questions correctly",bg=back,fg=fore,font=("David",18))
q1label=Label(body,text="Question one(1)Which planet is the biggest?", fg=fore, bg=back, font=("David",18))
q2label = Label(body, text="Question Two(2):what planet is the hottest?", fg=fore, bg=back, font=("David",18))
q3label = Label(body, text="Question three(3):what planet is the coldest?", fg=fore, bg=back, font=("David",18))
q4label = Label(body, text="Question Four(4):what planet is closest to the sun?", fg=fore, bg=back, font=("David",18))
q5label = Label(body, text="Question Five(5)what planet is Farthest from the sun?", fg=fore, bg=back, font=("David",18))
Q1bt = ttk.Button(body,text="CONFIRM", bootstyle='success', command=submit)
#Q2bt = Button(body,text="CONFIRM",fg='black',bg="White",command=submit)
#Q3bt = Button(body,text="CONFIRM",fg='black',bg="White",command=submit)
#Q4bt = Button(body,text="CONFIRM",fg='black',bg="White",command=submit)
#Q5bt = Button(body,text="CONFIRM",fg='black',bg="White",command=submit)
q1 = IntVar()
q2 = IntVar()
q3 = IntVar()
q4 = IntVar()
q5 = IntVar()
nameentry = Entry(body, font=("Verdana", 18))
numberEntery = Entry(body, font=("serifs", 18))
Q1a = ttk.Radiobutton(body, text="Jupiter",  variable=q1,value=1)
Q1b=ttk.Radiobutton(body,text="Neptune", variable=q1,value=2)
Q2a=ttk.Radiobutton(body,text="Mercury", variable=q2,value=1)
Q2b=ttk.Radiobutton(body,text="Venus", variable=q2,value=2)
Q3a=ttk.Radiobutton(body,text="Uranus", variable=q3,value=1)
Q3b=ttk.Radiobutton(body,text="Neptune", variable=q3,value=2)
Q4a=ttk.Radiobutton(body,text="Mercury", variable=q4,value=1)
Q4b=ttk.Radiobutton(body,text="Earth", variable=q4,value=2)
Q5a=ttk.Radiobutton(body,text="Mars", variable=q5,value=1)
Q5b=ttk.Radiobutton(body,text="Neptune", variable=q5,value=2)
heading.place(x=15,y=10)
namelabel.place(x=15,y=90)
nameentry.place(x=230,y=90)
numberLabel.place(x=540,y=90)
numberEntery.place(x=850,y=90)
question.place(x=250,y=130)
q1label.place(x=15,y=180)
q2label.place(x=15,y=240)
q3label.place(x=15,y=300)
q4label.place(x=15,y=360)
q5label.place(x=15,y=420)
Q1a.place(x=500,y=180)
Q1b.place(x=600,y=180)
Q2a.place(x=500,y=240)
Q2b.place(x=600,y=240)
Q3a.place(x=500,y=300)
Q3b.place(x=600,y=300)
Q4a.place(x=500,y=360)
Q4b.place(x=600,y=360)
Q5a.place(x=550,y=420)
Q5b.place(x=650,y=420)
Q1bt.place(x=500,y=500)
#Q2bt.place(x=750,y=240)
#Q3bt.place(x=750,y=300)
#Q4bt.place(x=800,y=360)
#Q5bt.place(x=850,y=420)
body.mainloop()