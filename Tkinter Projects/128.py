from tkinter import *

def con_miles():
    val = txtvalue.get()
    val = int(val)
    outmsg["text"] = str(round(val*1.6093, 2))+" kilometers"

def con_km():
    val = txtvalue.get()
    val = int(val)
    outmsg["text"] = str(round(val*0.6214, 2))+" miles"

val = 0

window = Tk()
window.title("EX 128")
window.geometry("480x240")
window["bg"] = "white"

lbltit = Label(text="Program to convert between Kilometres and Miles")
lbltit["justify"] = "center"
lbltit.place(x=0, y=5, width=480)

lblvalue = Label(text="Enter value to convert : ")
lblvalue["justify"] = "left"
lblvalue.place(x=100, y=40, width=125)
txtvalue = Entry(text=0, border=2)
txtvalue["justify"] = "center"
txtvalue.place(x=100+130, y=40, width=120)

btnmile = Button(text="Convert miles to km", command=con_miles)
btnmile.place(x=100, y=80)
btnkm = Button(text="Convert km to miles", command=con_km)
btnkm.place(x=100+130, y=80)

outmsg = Message(text=0)
outmsg["justify"] = "center"
outmsg["bg"] = "white"
outmsg.place(x=215, y=120)

window.mainloop()