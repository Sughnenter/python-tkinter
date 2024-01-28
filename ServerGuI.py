from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
front = "#104007"
back = "#3ae01d"


def selected(event):
    mylabel = Label(window, text=combo.get()).pack()
window = Tk()
window.geometry("800x450")
photo = PhotoImage(file="2882.png", )
button = Button(window, fg=front, height=197, width=156, bg=back, relief=RAISED, bd=10, text="Sham",font=('Helvetica bold', 18 ),image=photo, compound=TOP)
button.pack(padx=20, pady=20)
option = [
    "Monday",
    "Tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday"
]
clicked = StringVar()
clicked.set(option[0])
drop = OptionMenu(window, clicked, *option)
drop.pack()

combo = ttk.Combobox(window, values=option)
combo.current(0)
combo.bind("<<ComboboxSelected>>", selected)
combo.pack()
window.iconphoto(True, photo)

window.mainloop()