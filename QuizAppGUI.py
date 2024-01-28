from tkinter import *
from tkinter import messagebox as mb
from tkinter import colorchooser
from tkinter import ttk

back = "#f5ded6"
front = "#672c18"


def question_one():
    answers = ["cellulose cell wall", "Chlorophyll", "cell membrane", "large vacuole"]
    question_one_window = Tk()
    question_one_window.geometry("800x600")
    question_one_window.config(bg=back)

    label1 = Label(question_one_window, text="1.	Which of the following organelles is common to both plants and"
                                             " animal cells?", fg=front, bg=back,   font=('Helvetica bold', 15), pady=80)
    label1.pack()
    q1 = IntVar()
    for index in range(len(answers)):
        answer1 = Radiobutton(question_one_window, text=answers[index], bg=back, fg=front,
                              font=("Helvetica bold", 15), variable=q1,  value=index)


        answer1.pack()


window = Tk()
window.title("QUIZ APP")
window.geometry("800x600")

window.config(background=back)
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)

tab1.config(bg=back)
tab2 = Frame(notebook)
notebook.add(tab1, text="1")
notebook.add(tab2, text="2")
notebook.place(x=22, y=27)




b1 = Button(tab1, text="1", bg=front, fg=back, font=('Helvetica bold', 15), command=question_one)
b1.pack(expand=True, pady=250, padx=250)


icon = PhotoImage(file='Screenshot_2019-08-31-13-13-39-1.png')
window.iconphoto(True, icon)

window.mainloop()