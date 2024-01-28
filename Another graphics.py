#Create a canvas code that will get you at least four different shapes it shoild be located at the center of thr canvas=
from tkinter import *

body = Tk()
body.title("Graphics App")
body.geometry("800x600")
back = "#f5ded6"
front = "#672c18"
body.config(bg=back)
def clearcanv():
    canv.delete("all")
def drawcirce():
    clearcanv()
    canv.create_oval(250,250,120,120,outline="black",fill=front)
def drawRect():
    clearcanv()
    canv.create_rectangle(300,250,155,155,outline="black",fill=front)
def drawsquare():
    clearcanv()
    canv.create_rectangle(300,300,150,150,outline="black",fill=front)
def drawtriangle():
    clearcanv()
    canv.create_polygon(180,230,380,80,380,230,outline="black",fill=front)
def drawstar():
    clearcanv()
    canv.create_polygon(160,160,190,160,200,130,210,160,240,160,215,180,225,210,200,190,175,210,185,180,outline='black',fill=front)
def drawdiamond():
    clearcanv()
    canv.create_polygon(245,100,145,225,245,350,345,225,245,100,outline="black",fill=front)
def drawpentagon():
    clearcanv()
    canv.create_polygon(250,100,120,225,120,350,380,350,380,225,250,100,outline="black",fill=front)

frame1 = Frame(body,bg=back,height=100,width=780)
frame1b = Frame(body,bg="#ecbcac",height=40,width=780)
frame2 = Frame(body,bg=back,height=500,width=780)
menubar = Menu(body)
filemenu = Menu(menubar)
editmenu = Menu(menubar)
helpmenu = Menu(menubar)
viewmenu = Menu(menubar)
#Menu items
filemenu.add_command(label="New File")
filemenu.add_separator()
filemenu.add_command(label="Details")
filemenu.add_separator()
filemenu.add_command(label="File details")
menubar.add_cascade(label="File",menu=filemenu)

editmenu.add_command(label="Change Colour")
editmenu.add_separator()
editmenu.add_command(label="Font")
filemenu.add_separator()
editmenu.add_command(label="File name")
menubar.add_cascade(label="edit",menu=editmenu)

helpmenu.add_command(label="About app")
helpmenu.add_separator()
helpmenu.add_command(label="Exit")
helpmenu.add_separator()
helpmenu.add_command(label="File details")
menubar.add_cascade(label="Help",menu=helpmenu)

viewmenu.add_command(label="File size")
viewmenu.add_separator()
viewmenu.add_command(label="File Length")
viewmenu.add_separator()
viewmenu.add_command(label="Layout")
menubar.add_cascade(label="view",menu=viewmenu)
body.config(menu=menubar)


label1 = Label(frame1,text="SIMPLE GRAPHICS",font=("Geometr415 Blk BT",36),fg=front,bg=back)
button1 = Button(frame1b,text="circle",font=("Helvertica bold",14),fg="white",bg=front,command=drawcirce)
button2 = Button(frame1b,text="Rectangle",font=("Helvertica bold",14),fg="white",bg=front,command=drawRect)
button3 = Button(frame1b,text="Square",font=("Helvertica bold",14),fg="white",bg=front,command=drawsquare)
button4 = Button(frame1b,text="Triangle",font=("Helvertica bold",14),fg="white",bg=front,command=drawtriangle)
button5 = Button(frame1b,text="Star",font=("Helvertica bold",14),fg="white",bg=front,command=drawstar)
button6 = Button(frame1b,text="Diamond",font=("Helvertica bold",14),fg="white",bg=front,command=drawdiamond)
button7 = Button(frame1b,text="Pentagon",font=("Helvertica bold",14),fg="white",bg=front,command=drawpentagon)


scrollbar = Scrollbar(frame2)
canv = Canvas(frame2,bg= "#ecbcac",height=450,width=500,bd=3,scrollregion=(0,0,1000,1000))
frame1.propagate(0)
frame1b.propagate(0)
frame2.propagate(0)
frame1.pack(padx=10)
frame1b.pack(padx=10)
frame2.pack(padx=10)
label1.pack(side="top")
button1.pack(side="left")
button2.pack(side="left",padx=10)
button3.pack(side="left",padx=10)
button4.pack(side="left",padx=10)
button5.pack(side="left",padx=10)
button6.pack(side="left",padx=10)
button7.pack(side="left",padx=10)
scrollbar.pack(side="right",fill=Y)
canv.pack(pady=30,fill=BOTH)
scrollbar.config(command=canv.yview)

body.mainloop()