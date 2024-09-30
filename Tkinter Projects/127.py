from tkinter import *

def addname():
    name = txtname.get()
    list_box.insert(END,name)

def clearname():
    list_box.delete(0,END)

window = Tk()
window.title("EX 127")
window.geometry("480x360")
window["bg"] = "white"

lbltit = Label(text="Program to add names to listbox")
lbltit["justify"] = "center"
lbltit.place(x=0, y=5, width=480)

lblname = Label(text="Enter name : ")
lblname["justify"] = "left"
lblname.place(x=40, y=40, width=120)
txtname = Entry(text=0, border=2)
txtname["justify"] = "center"
txtname.place(x=40, y=80, width=120)

lblnamelist = Label(text="Name list : ")
lblnamelist.place(x=300, y=40, width=120)
list_box = Listbox()
list_box.place(x=300, y=80, width=120)

btnadd = Button(text="Add name", command=addname)
btnadd.place(x=60, y=120)
btnclear = Button(text="Clear list", command=clearname)
btnclear.place(x=150, y=120)

window.mainloop()