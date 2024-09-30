from tkinter import *

def Call():
    msg = Label(window, text = "You pressed the button")
    msg.place(x = 30, y = 50)
    button["bg"] = "red"
    button["fg"] = "white"

window = Tk()
window.geometry("1920x1280")
button = Button(text = "Press me", command = Call)
button.place(x = 30, y = 20, width = 120, height = 25)
window.mainloop()