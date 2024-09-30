from tkinter import *

def add():
        num = txtadd.get()
        num = int(num)
        total = txttot["text"]
        total = int(total)
        total = num + total
        txttot["text"] = str(total)

def rst():
    txtadd.delete(0, END)
    txttot["text"] = 0

num = 0
total = 0

window = Tk()
window.title("EX 126")
window.geometry("480x360")
window["bg"] = "white"

lbltit = Label(text="Program to add and reset")
lbladd = Label(text="Enter number to add : ")
lbltot = Label(text="Total : ")
txtadd = Entry(text=0, border=2)
txttot = Message(text=0, border=2)
btnadd = Button(text="Add", command=add)
btnrst = Button(text="Reset", command=rst)

lbltit["justify"] = "center"
lbltit.place(x=0, y=10, width=480)
lbladd["justify"] = "left"
lbladd.place(x=40, y=40, width=120)
txtadd["justify"] = "center"
txtadd.place(x=40, y=80, width=120)
lbltot["justify"] = "right"
lbltot.place(x=300, y=40, width=120)
txttot["justify"] = "center"
txttot.place(x=300, y=80, width=120)

btnadd["justify"] = "center"
btnadd.place(x=120, y=120, width=80)
btnadd["justify"] = "center"
btnrst.place(x=220, y=120, width=80)

window.mainloop()