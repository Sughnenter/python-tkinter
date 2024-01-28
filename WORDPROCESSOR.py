import sys
import re
from tkinter import *
import collections
from tkinter import messagebox as mb
import ttkbootstrap as ttk
body=Tk()
body.title("Word Processor")
body.geometry("800x480")
mb = Menu(body)
back="#D5EAF1"
front="#872F30"
#definition of buttons
def words():
    data=text1.get("1.0",END)
    word=(data.split())
#    mb.showwarning("Warning", "Do you want to exit")
    label2.config(text=f"The words used are {word}")

def search():
    data = text1.get("1.0", END)
    search=str(data.find(data))
    label2.config(text=f"{search}")

#def Findall_ch():
    dat=text1.get("1.0", END)
    data=re.findall('\D', dat)
    label2.config(text=f"There are {data} characters in the text.")


def findall_cha_len():
    data=text1.get("1.0",END)
    w=re.findall('\D', data)
    word=len(w)
    label2.config(text=f"There are {word} characters in the text.")


def Findall_letters():
    zi=text1.get("1.0", END)
    jj=re.findall('[a-zA-Z]', zi)
    jjj=len(jj)
    label2.config(text=f"The total words used are {jjj}")

def search():
    tt=text2.get()
    data=text1.get("1.0", END)
    gotcha=(re.findall(tt,data))
    no=len(gotcha)
    label2.config(text=f"'{tt}' is found {no} time(s) in the information")

def replace():
    oo=text3.get()
    dar=text1.get("1.0", END)
    h=text4.get()
    gotcha=(re.sub(h,oo, dar))
    no=text1.get("1.0", END)
  #  text1.config(text=f"{gotcha}")
    label2.config(text=f"'{h}' succesfully interchanged with '{oo}'. \n it's now wriiten as '{gotcha}'")
 #   print(gotcha)
def exit():

    sys.exit()

def open_f():
    msbody = open("msworD.txt", "w")
    msbody.write(text1.get("1.0",END))
    msbody.close()
def open_s():
    msbody = open("msworD.txt", "r")
    ct=msbody.read()
    text1.insert(END, ct)
    msbody.close()
def new_f():
    msbody = open("msworD.txt", "w")
    msbody.write(text1.get(1.0, END))
    msbody.close()

filemenu = ttk.Menu(mb)
fimenu = Menu(mb)
editmenu = Menu(mb)
viewmenu = Menu(mb)
runmenu = Menu(mb)
helpmenu = Menu(mb)
filemenu.add_command(label="Save",command=open_f)
filemenu.add_separator()
filemenu.add_command(label="Open",command=open_s)
mb.add_cascade(label="File", menu=filemenu)
editmenu.add_command(label="Total number of words",command=Findall_letters)
editmenu.add_command(label="Total number of characters",command=findall_cha_len)
mb.add_cascade(label="Find", menu=editmenu)
runmenu.add_command(label="Undo")
runmenu.add_command(label="Watermarks")
runmenu.add_command(label="Paragraph Spacing")
runmenu.add_command(label="Page Colour")
mb.add_cascade(label="Edit", menu=runmenu)
helpmenu.add_command(label="Press F1 for enquires")
mb.add_cascade(label="Help", menu=helpmenu)
fimenu.add_command(label="Exit",command=exit)
mb.add_cascade(label="Exit", menu=fimenu)

body.config(menu=mb)

frame1=Frame(body,bg=back,height=270,width=700)
frame1b=Frame(body,bg=back,height=40, width=700)
frame2=Frame(body,bg=back,height=140,width=700)
frame2b=Frame(body,bg=back,height=80,width=700)
sc=Scrollbar(frame1)


label1=Label(frame1,text="WORD PROCESSOR",bg=back,fg=front,font=("Aerial",40))
label2=Label(frame1b,text="Message",bg=back,fg=front,font=("Aerial",14))
text1=Text(frame1,yscrollcommand=sc.set, font=('Aerial',14))
text2=Entry(frame2, font=('Aerial',10))
text3=Entry(frame2b, font=('Aerial',10))
label3=Label(frame2b,text="With",bg="#660E1D",fg="white",font=("Aerial",17))
text4=Entry(frame2b, font=('Aerial',8))



#buttons
button1=Button(frame2,text="Findall words",bg="#660E1D",fg="white",font=("Aerial",14),command=words)
button2=Button(frame2,text="Findall characters",bg="#660E1D",fg="white",font=("Aerial",14),command = findall_cha_len)
button3=Button(frame2,text="Search",bg="#660E1D",fg="white",font=("Aerial",14),command=search)
button5=Button(frame2b,text="Replace",bg="#660E1D",fg="white",font=("Aerial",14),command=replace)



#frame propagation
frame1.propagate(0)
frame1b.propagate(0)
frame2.propagate(0)
frame2b.propagate(0)
frame1.pack(padx=10)
frame1b.pack()

frame2.pack(pady=15)
frame2b.pack()
label1.pack()
label2.pack()

text1.pack()
button1.pack(side="left")
button5.pack(side="left",padx=10)
text4.pack(side="left",padx=5)
label3.pack(side="left",padx=5)
text3.pack(side="left")
button2.pack(side="left",padx=10)
button3.pack(side="left",padx=10)
text2.pack(side="left")
sc.pack(side="right", fill=Y)
text1.pack(fill=BOTH)
sc.config(command=text1.yview)

body.mainloop()