from tkinter import *

def addnum():
    num = txtnum.get()
    if num.isdigit():
        list_box.insert(END,num)
    else:
        txtnum["text"] = 0

def clearnum():
    list_box.delete(0,END)

def savenum():
    tmp_list = list_box.get(0,END)

    file = open("num.csv","w")
    x=0
    for row in tmp_list:
        data = tmp_list[x]+"\n"
        file.write(data)
        x = x+1
    file.close()

num = 0

window = Tk()
window.title("EX 127")
window.geometry("480x360")
window["bg"] = "white"

lbltit = Label(text="Program to add only whole numbers to listbox")
lbltit["justify"] = "center"
lbltit.place(x=0, y=5, width=480)

lblnum = Label(text="Enter a number : ")
lblnum["justify"] = "left"
lblnum.place(x=40, y=40, width=120)
txtnum = Entry(text=0, border=2)
txtnum["justify"] = "center"
txtnum.place(x=40, y=80, width=120)

lblnumlist = Label(text="Number list : ")
lblnumlist.place(x=300, y=40, width=120)
list_box = Listbox()
list_box.place(x=300, y=80, width=120)

btnadd = Button(text="Add number", command=addnum)
btnadd.place(x=40, y=120)
btnclear = Button(text="Clear list", command=clearnum)
btnclear.place(x=130, y=120)
btnsave = Button(text="Save", command=savenum)
btnsave.place(x=80, y=160, width=80)

window.mainloop()