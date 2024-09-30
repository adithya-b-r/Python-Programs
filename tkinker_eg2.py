from tkinter import *

def call():
    msg = Label(window, text = "You pressed a button!")
    msg.place(x = 30, y = 50)
    Button["bg"] = "blue"
    Button["fg"] = "white"

window = Tk()
window.geometry("200x110")
Button = Button(text = "Press me", command = call)
Button.place(x = 30, y = 20, width = 120, height = 25)
window.mainloop()
