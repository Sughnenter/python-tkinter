import Rand as rd
from tkinter import *
def allocate():
    name =NameEntry.get()
    if name != "" :
        info = (rd.randint(0,1000))
    output = f"OUTPUT\n {name}'s  student number is " + str(info)
    FTlabel.config(text=output)
window = Tk()
window.title("Allocator App")
window.geometry("700x500")
window.config(bg="green")
myText = Label(window, text="Number Allocator", fg="white", bg="green", font=("Verdana"))
NameLabel = Label(window, text="Student Name", fg="white", bg="green", font=("Verdana"))
#Ratelabel = Label(window, text="RATE", fg="white", bg="blue", font=("Verdana"))
FTlabel = Label(window, text="Student Number", fg="white", bg="green", font=("Verdana"))
# ENTRIES
NameEntry = Entry(window, font=("Verdana", 18), width=20)
#RateEntry = Entry(window, font=("verdana", 18), width=20)
# BUTTONS
give = Button(window, text="ALLOCATE", font=("Tahoma", 18), command=allocate)
myText.place(x=15,y=10)
NameLabel.place(x=15,y=55)
NameEntry.place(x=15,y=90)
give.place(x=15,y=145)
FTlabel.place(x=340,y=55)
window.mainloop()