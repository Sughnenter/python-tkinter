from tkinter import *
def convert():
   cm = CMEntry.get()
   rate = RateEntry.get()
   if cm != "" and rate != "":
       fig = int(cm)/int(rate)
   output = "CONVERT\n"+str(fig)
   result.config(text=output)

window = Tk()
window.title("Converter App")
window.geometry("800x600")
window.config(bg="blue")
myText = Label(window, text= "HEIGHT CONVERTER",fg="white",bg="blue",font=("Verdana"))
CMLabel = Label(window,text="HEIGHT(CM)",fg="white",bg="blue",font=("Verdana"))
Ratelabel = Label(window, text= "RATE",fg="white",bg="blue",font=("Verdana"))
FTlabel = Label(window,text="HEIGHT(FT)",fg = "white",bg="blue",font=("Verdana"))
#ENTRIES
CMEntry = Entry(window,font=("Verdana",18),width=20)
RateEntry = Entry(window,font=("verdana",18),width=20)
#BUTTONS
Convert = Button(window, text="CONVERT",font=("Tahoma",18),command = convert)
#For pack
myText.pack(pady=5)
#CMLabel.pack(pady=5)
#CMEntry.pack()
#Ratelabel.pack(pady=5)
#RateEntry.pack()
#Convert.pack(pady=10)
#FTlabel.pack(pady=5)
#For Grid
myText.grid(row=0,column=0,columnspan=3,sticky='EW',pady=5)
CMLabel.grid(row=1,column=0,sticky='E')
CMEntry.grid(row=1,column=1,columnspan=2)
Ratelabel.grid(row=2,column=0,sticky='E')
RateEntry.grid(row=2,column=1,columnspan=2,pady=5)
Convert.grid(row=3,column=1,columnspan=2,sticky='EW',pady=5)
FTlabel.grid(row=4,column=1,pady=5)
window.mainloop()
