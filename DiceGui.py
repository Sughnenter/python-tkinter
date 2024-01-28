import Rand as rd
from tkinter import messagebox as mb
from tkinter import *

# FUNCTIONS


def roll():
    p1 = entry_1.get()
    scores = [0]
    active_player = 1
    number_of_trials = 5
    rack = [1, 2, 3, 4, 5, 6]
    output = f"{p1}'s turn to roll \n (press roll)"
    output_label.config(text=output)
    die = rd.choice(rack)
    mb.showinfo("DIE ROLLED", f"You rolled a {die} ")
    output = f"{p1} rolled a {die}"
    output_label.config(text=output)

    if die == 6 and scores[active_player-1] == 0:
        output = f"{p1}'s \n score starts counting"
        score_label.config(text=output)
        scores[active_player-1] = 6
    elif scores[active_player-1] > 0:
        output = f"{p1} scores {die}"
        score_label.config(text=output)
        scores[active_player-1] += die
    while number_of_trials > 0 < 5:
        number_of_trials -= 1
        output = f"{p1} plays {die}\n scores {scores}"
        score_label.config(text=output)
        output = f" {p1} has {number_of_trials} trials left"
        score_label.config(text=output)




def roll_2():
    p2 = entry_2.get()
    scores = [0]
    active_player = 1
    number_of_trials = 5
    rack = [1, 2, 3, 4, 5, 6]
    output = f"{p2}'s turn to roll \n (press roll)"
    die = rd.choice(rack)
    mb.showinfo("DIE ROLLED", f"{p2} rolled a {die} ")
    output = f"{p2} rolled a{die}"
    output_label.config(text=output)


window = Tk()
window.title("Dice Game")
window.geometry("1000x450")
back = "#3ea865"
front = "black"
bg = back
fg = front
# FRAMES
top_frame = Frame(window, bg="Black", height=50, width=1000)
left_frame = Frame(window, bg=back, height=400, width=500)
right_frame = Frame(window, bg="#42403a", height=400, width=250)
right_frame_b = Frame(window, bg=back, height=400,width=250)
# bottom_frame = Frame(window, bg=back, height=0, width=0)

# LABELS
title_label = Label(top_frame, text="DICE GAME", bg="Black", fg="white", font=('Helvetica bold', 20))
output_tittle = Label(top_frame, text="OUTPUT", bg="black", fg="white", font=('Helvetica bold', 20))
score_tittle = Label(top_frame, text="SCORE", bg="black", fg="white", font=('Helvetica bold', 20))
label_1 = Label(left_frame, text="Enter your player name", bg=back, fg=front, font=('Helvetica bold', 18))
label_2 = Label(left_frame, text="Enter your player name", bg=back, fg=front, font=('Helvetica bold', 18))
output_label = Label(right_frame, text="OUTPUT", bg="#42403a", fg="White", font=('Helvetica bold', 14))
score_label = Label(right_frame_b, text="SCORES", bg=back, fg=front, font=('Helvetica bold', 14))
# ENTRIES
entry_1 = Entry(left_frame, font=('Helvetica Bold', 14))
entry_2 = Entry(left_frame, font=('Helvetica Bold', 14))
# BUTTONS
button_1 = Button(left_frame, text="Roll", bg=front, fg="white", font=('Helvetica bold', 12), command=roll)
button_2 = Button(left_frame, text="Roll", bg=front, fg="white", font=('Helvetica bold', 12), command=roll_2)
# Frame Propagations
top_frame.propagate(0)
right_frame.propagate(0)
right_frame_b.propagate(0)
left_frame.propagate(0)
# PLACEMENT
top_frame.pack()
left_frame.pack(side=LEFT)
right_frame_b.pack(side=RIGHT)
right_frame.pack(side=RIGHT)

title_label.place(x=200, y=10)
output_tittle.place(x=575, y=10)
score_tittle.place(x=800, y=10)
label_1.place(x=10, y=35)
entry_1.place(x=270, y=35)
button_1.place(x=150, y=75)
label_2.place(x=10, y=120)
entry_2.place(x=270, y=120)
button_2.place(x=150, y=170)
output_label.place(x=15, y=15)
score_label.place(x=15, y=15)


window.mainloop()