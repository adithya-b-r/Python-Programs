from tkinter import *

def newFile():
    file = open("ages.csv","w")
    file.close()

def addFile():
    file = open("ages.csv","a")
    name = entname.get()
    name = str(name)
    age = entage.get()
    age = str(age)
    data = name+", "+age+"\n"
    file.write(data)
    file.close()

window = Tk()
window.title("EX 131")
window["bg"] = "white"
window.geometry("480x240")

lbltit = Label(text="Program to save data to .csv file")
lbltit["justify"] = "center"
lbltit.place(x=0, y=5, width=480)

lblname = Label(text="Enter name : ")
lblname["justify"] = "left"
lblname.place(x=10, y=40)
lblage = Label(text="Enter age : ")
lblage["justify"] = "right"
lblage.place(x=250, y=40)

entname = Entry()
entname["justify"] = "center"
entname.place(x=90, y=42)
entage = Entry()
entage["justify"] = "center"
entage.place(x=320, y=42)

btnnew = Button(text="New File", command=newFile)
btnnew.place(x=120, y = 80, width=100)
btnadd = Button(text="Add to file", command=addFile)
btnadd.place(x=240, y = 80, width=100)

window.mainloop()