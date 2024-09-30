from tkinter import *

def add():
    num1 = textbox1.get()
    num2 = textbox2.get()
    num1 = int(num1)
    num2 = int(num2)
    #print(num1+num2)
    add = num1+num2
    add = str(add)
    textbox3["text"] = add

window = Tk()
window.geometry("500x300")

label1 = Label(text = "First number : ")
label1.place(x = 30, y = 10)

textbox1 = Entry(text = "")
textbox1.place(x = 150, y = 10)
textbox1["justify"] = "center"

label2 = Label(text = "Second number : ")
label2.place(x = 30, y = 40)

textbox2 = Entry(text = "")
textbox2.place(x = 150, y = 40)
textbox2["justify"] = "center"

button1 = Button(text = "Add", command = add)
button1.place(x = 30, y = 70, width = 100, height = 25)

textbox3 = Message(text = "")
textbox3.place(x = 150, y = 70, height = 25, width = 120)
textbox3["bg"] = "white"
textbox3["relief"] = "sunken"
textbox3["justify"] = "center"

window.mainloop()