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

def dispFile():
    disp_list.delete(0,END)
    file = open("ages.csv","r")
    for row in file:
        disp_list.insert(END,row)
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
lblage.place(x=10, y=70)

entname = Entry(border=2)
entname["justify"] = "center"
entname.place(x=90, y=42)
entage = Entry(border=2)
entage["justify"] = "center"
entage.place(x=90, y=72)

btnnew = Button(text="New File", command=newFile)
btnnew.place(x=10, y = 110, width=100, height=30)
btnadd = Button(text="Add to file", command=addFile)
btnadd.place(x=130, y = 110, width=100, height=30)
btndisp = Button(text="Display contents", command=dispFile)
btndisp.place(x=70, y=150, width=100, height=30)

disp_list = Listbox()
disp_list.place(x=300, y=40)

window.mainloop()